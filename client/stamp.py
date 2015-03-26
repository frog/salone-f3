from rpigl import glesutils,transforms

class Stamp:
    
    def __init__(self, outcome, gameWindow):
        self.outcome = outcome
        if outcome is "fact":
            self.filename = "fact.tga"
            self.endpoint = "voteFact"
        elif outcome is "fiction":
            self.filename = "fiction.tga"
            self.endpoint = "voteFiction"
        else:
            raise ValueError("Invalid stamp outcome: %s" % outcome)
        
        self.texture_data = glesutils.TextureData.from_file("images/"+self.filename)
        self.texture = glesutils.Texture.from_data(self.texture_data)
        
        self.matrix = transforms.translation(0,0,0)
        
        #precompute rotoscale 
        self.rotoscaleIn = transforms.stretching(1, 1/gameWindow.actual_w_to_h_ratio, 1)
        
        scaleX = self.texture_data.width / 2 / float(gameWindow.width);
        scaleY = self.texture_data.height / 2 / float(gameWindow.height);
        self.rotoscaleIn = transforms.compose(transforms.stretching(scaleX, scaleY, 1), self.rotoscaleIn)
        
        self.rotoscaleOut = transforms.stretching(1, gameWindow.actual_w_to_h_ratio, 1)
        
        #intial values
        self.alpha = 1.0;
        self.rot = 0;
        self.zoom = 1.0;
    
    def bindOn(self, textureID):
        self.texture.bind(textureID)
    
    def setAlpha(self, alpha):
        self.alpha = alpha
        
    def setRotation(self, rot):
        self.rot = rot
        
    def setZoom(self, zoom):
        self.zoom = zoom
        
    def draw(self, gameWindow):
        self.bindOn(2)
        gameWindow.program.uniform.texture.value = 2
        zoomed = transforms.compose(self.rotoscaleIn, gameWindow.base_matrix)
        
        gameWindow.program.uniform.alpha.value = self.alpha
        zoomed = transforms.compose(transforms.scaling(self.zoom), zoomed)
        zoomed = transforms.compose(transforms.rotation_degrees(self.rot, "z"), zoomed)
        
        zoomed = transforms.compose(self.rotoscaleOut, zoomed)
        gameWindow.mvp_mat.value = zoomed
        gameWindow.drawing.draw()