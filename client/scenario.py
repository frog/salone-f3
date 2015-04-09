from rpigl import glesutils, transforms
from rpigl.gles2 import *
import threading
import json    
import urllib2

class Scenario:

    def __init__(self, id, imagePath):
        self.id = id #string
        self.imagePath = imagePath #string
        self.texture = None
        self.loadEvent = threading.Event()
        self.textureID = -1 #not bound
        
    def isReady(self):
        return self.texture != None
    
    def bindOn(self, textureID):
        if self.textureID < 0 or self.textureID != textureID:
            self.texture.bind(textureID)
            self.textureID = textureID
        
    def loadTexture(self, sync =True):
        if not self.isReady():
            def worker(num):
                self.loadEvent.texture_data = glesutils.TextureData.from_file("images/"+num)
                print "Texture Data loaded, signaling"
                self.loadEvent.set()
            threading.Thread(target=worker, args=(self.imagePath,)).start()   
            
        if sync:
            while not self.loadEvent.isSet():
                #if not loaded then wait to be loaded
                self.loadEvent.wait()
            
            #this is quick
            self.texture = glesutils.Texture.from_data(self.loadEvent.texture_data)
            print "Texture loading done."
        
    def unloadTexture(self):
        #not sure what happens here, setting the world to null
        if self.loadEvent != None:
            self.loadEvent.texture_data = None
            self.loadEvent = None
        
        self.texture = None
        self.textureID = -1
        self.loadEvent = threading.Event()
        
    def vote(self, fof):           
        def worker(id, fof):            
            f = urllib2.urlopen('https://f3.cloud.frogdesign.com/vote'+fof+'/'+id)
            print "Signaled"
            print f.read(50)
            f.close()
        threading.Thread(target=worker, args=(self.id,fof,)).start()   
        

class Scenarios:
    
    current = 0
    list = []
    
    @staticmethod
    def parseAndLoad():
        with open("../server/spreads.json") as json_file:
            json_data = json.load(json_file)
            for a in json_data:
                tga_name = a['spreadId']+'.tga'
                Scenarios.list.append(Scenario(a['spreadId'], tga_name))
                print(a['spreadId'], tga_name)
    
    @staticmethod
    def getCurrent():
        return Scenarios.list[Scenarios.current]
        
    @staticmethod
    def getPrevious():
        idx = Scenarios.current - 1
        if idx < 0:
            idx = len(Scenarios.list) - 1
        return Scenarios.list[idx]
        
    @staticmethod
    def advance():
        next = Scenarios.current + 1;
        if next >= len(Scenarios.list):
            next = 0
        Scenarios.current = next
        
    @staticmethod
    def getNext():
        idx = Scenarios.current + 1;
        if idx >= len(Scenarios.list):
            idx = 0
        return Scenarios.list[idx]
        
    @staticmethod
    def preload(sync =True):
        for i in range(0,3):
            Scenarios.list[Scenarios.current + i].loadTexture(sync)


