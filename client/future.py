import pygame, signal, pigpio
import sys, traceback
from rpigl import glesutils, transforms
from rpigl.gles2 import *
from scenario import *
from animation import *
from pygame.locals import *
from stamp import *
from time import sleep
import urllib2

pi = pigpio.pi()
PIR_PIN_KO = 4
PIR_PIN_OK = 17
pi.set_mode(PIR_PIN_KO, pigpio.INPUT)
pi.set_mode(PIR_PIN_OK, pigpio.INPUT)
pi.set_pull_up_down(PIR_PIN_KO, pigpio.PUD_UP)
pi.set_pull_up_down(PIR_PIN_OK, pigpio.PUD_UP)

pygame.init();

# A GLSL (GL Shading Language)  program consists of at least two shaders:
# a vertex shader and a fragment shader.
# Here is the vertex shader.
vertex_glsl = """
uniform mat4 mvp_mat; // a uniform is an input to the shader which is the same for all vertices

attribute vec2 vertex_attrib; // an attribute is a vertex-specific input to the vertex shader
attribute vec2 texcoord_attrib; // an attribute is a vertex-specific input to the vertex shader

varying vec2 texcoord_var;  // a varying is output to the vertex shader and input to the fragment shader

void main(void) {
  gl_Position = mvp_mat * vec4(vertex_attrib, 0.0, 1.0);
  texcoord_var = texcoord_attrib;
}
"""

# Here is the fragment shader
fragment_glsl = """
uniform sampler2D texture; // access the texture
uniform float alpha; // access the texture
varying vec2 texcoord_var;
void main(void) {
  gl_FragColor = texture2D(texture, texcoord_var);
  gl_FragColor.a = alpha;
}
"""

# The array spec: names and formats of the per-vertex attributes
#   vertex_attrib:2h  = two signed short integers  
#   color_attrib:3Bn  = three unsigned bytes, normalized (i.e. shader scales number 0..255 back to a float in range 0..1)
array_spec = glesutils.ArraySpec("vertex_attrib,texcoord_attrib:2f")

class Future(glesutils.GameWindow):
    framerate = 60
    angle = 0
    program = None

    def init(self):
        """All setup which requires the OpenGL context to be active."""
        
        self.currentScenario = 0
        self.animation = []
        self.okpressed = 0
        self.kopressed = 0
        
        # compile vertex and fragment shaders
        vertex_shader = glesutils.VertexShader(vertex_glsl)
        fragment_shader = glesutils.FragmentShader(fragment_glsl)
        # link them together into a program
        program = glesutils.Program(vertex_shader, fragment_shader)
        # set the background to RGBA = (1, 0, 0, 1) (solid red)
        #glClearColor(1, 0, 0, 0)

        # set up pre-multiplied alpha
        glEnable(GL_BLEND)
        glBlendFunc(GL_ONE, GL_ONE_MINUS_SRC_ALPHA)
        
        glDisable(GL_DEPTH_TEST)

        # load uniforms
        self.mvp_mat = program.uniform.mvp_mat
        self.mvp_mat.value = transforms.rotation_degrees(0, "z")

        # bind uniform named "texture" to texture unit 1
        # normally, when using only one texture, 0 would be more logical,
        # but this is just for demo purposes
        program.uniform.texture.value = 0 # bind texture to texture unit 1
        program.uniform.alpha.value = 1.0
        
        self.actual_w_to_h_ratio = float(self.width) / float(self.height)
        print("WtoH ratio", self.actual_w_to_h_ratio)
        # data for the three vertices
        y_min = 0.70;
        positions = ((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))
        elements = (0,1,2,0,2,3)
        # create an array buffer from the spec
        # note: all buffer objects are automatically bound on creation
        self.drawing = array_spec.make_drawing(vertex_attrib=positions, elements=elements)
        
        # use the program, bind the texture
        program.use()
        self.program = program

        # print some OpenGL implementation information
        version = glesutils.get_version()
        for k in version.__dict__:
            print("%s: %s" % (k, getattr(version, k)))
            
        self.base_matrix = transforms.scaling(2)
        self.base_matrix = transforms.compose(transforms.translation([-1, -1, 0]), self.base_matrix)
        self.base_matrix = transforms.compose(transforms.rotation_degrees(180, "z"), self.base_matrix)
        self.translation = transforms.translation([0, 0, 0])
        self.mvp =  transforms.compose(self.translation, self.base_matrix)
        
        #for s in Scenarios:
        #    s.loadTexture()
        
        print "Before Preloading"
        Scenarios.preload()
        print "Pre-loaded"
        
        self.fact = Stamp("fact", self)
        self.fiction = Stamp("fiction", self)
        self.currentStamp = None

    def doneAnimation(self, anim):
        print "Done Animation"
        self.animation.remove(anim)
        self.currentStamp = None
        Scenarios.getPrevious().unloadTexture
        Scenarios.getNext().loadTexture(True)

    def doneAnimation2(self, anim):
        self.animation.remove(anim)
        
    def on_frame(self, time):
        for a in self.animation:
            a.update()
            
        self.redraw()
        if len(self.animation) == 0:
            if self.kopressed == 0:
                self.kopressed = pi.read(PIR_PIN_KO)
                if self.kopressed == 1:
                    print "KO!"                
                    self.currentStamp = self.fiction
                    Scenarios.getCurrent().vote('Fiction')
                    self.goOn()
            else:
                self.kopressed = pi.read(PIR_PIN_KO)
                
            if self.okpressed == 0:
                self.okpressed = pi.read(PIR_PIN_OK)
                if self.okpressed == 1:
                    print "OK!"
                    self.currentStamp = self.fact
                    Scenarios.getCurrent().vote('Fact')
                    self.goOn()
            else:
                self.okpressed = pi.read(PIR_PIN_OK)
            
        
    def on_quit(self, event): 
        self.done = True
        
    def on_keydown(self, event):
        #print event
        if event.key == K_ESCAPE:
            self.done = True
        elif event.key == K_RIGHT:
            self.goOn()
                

    def draw(self):
        time = pygame.time.get_ticks()
        
        if len(self.animation) > 0:
            self.program.uniform.alpha.value = 1.0
            s = Scenarios.getPrevious()
            s.bindOn(1)
            self.program.uniform.texture.value = 1
            #self.translation[1,3] = - game.translate
            #self.mvp_mat.value = transforms.compose(self.translation, self.base_matrix)
            self.mvp_mat.value = self.base_matrix;
            self.drawing.draw()
                        
            if not self.currentStamp is None: 
                self.currentStamp.draw(self)
            
            s = Scenarios.getCurrent()
            s.bindOn(0)
            self.program.uniform.alpha.value = 1.0
            self.program.uniform.texture.value = 0
            self.translation[1,3] = 2.0 - game.translate
            self.mvp_mat.value = transforms.compose(self.translation, self.base_matrix)
            #self.mvp_mat.value = self.mvp;
            self.drawing.draw()
        else:                        
            s = Scenarios.getCurrent()
            s.bindOn(0)
            self.program.uniform.alpha.value = 1.0
            self.program.uniform.texture.value = 0
            self.translation[1,3] = 0
            self.mvp_mat.value = transforms.compose(self.translation, self.base_matrix)
            #self.mvp_mat.value = self.base_matrix
            self.drawing.draw()         
            
        self.mvp_mat.value = self.base_matrix;
        #print "Time: ", pygame.time.get_ticks() - time
        
    def goOn(self):
        
        Scenarios.advance()
        Scenarios.getCurrent().loadTexture()
        animation = SlideAnimation(self.doneAnimation);
        stampAnimation = StampAnimation(self.doneAnimation2);
        self.animation.append(animation)
        self.animation.append(stampAnimation)
        animation.start()
        stampAnimation.start()
        
class SlideAnimation(Animation):
    
    def __init__(self, callback):
        Animation.__init__(self, 1000, 0.0, 2.0, 1000)
        self.callback = callback

    def onTick(self, value):
        game.translate = value

    def onEnd(self):
        game.translate = 1.0
        self.callback(self)
        
class StampAnimation(Animation):
    
    def __init__(self, callback):
        Animation.__init__(self, 500, 0.0, 1.0)
        self.callback = callback

    def onTick(self, value):
        if not game.currentStamp is None:
            game.currentStamp.setZoom(value)
            game.currentStamp.setAlpha(value) 
            game.currentStamp.setRotation(int(35 * value)) 

    def onEnd(self):
        self.callback(self)

#cleanly exit
def cleanExit():
    pygame.quit()
    sys.exit(0)
    pi.stop()
    
# Handling Ctrl+C to provide cleanup
def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    cleanExit()
signal.signal(signal.SIGINT, signal_handler)



Scenarios.parseAndLoad()

try:
    game = Future(640, 480, pygame.RESIZABLE)
    game.translate = 0.0
    game.run()
except Exception, err:
    traceback.print_exc()
    cleanExit()
 
cleanExit()