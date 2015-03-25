import pygame, math

class Animation:
    CREATED = 0
    STARTED = 1
    ENDED = 2
    def __init__(self, duration, start_value, end_value):
        self.duration = duration
        self.start_value = start_value
        self.end_value = end_value
        self.state = Animation.CREATED
        
    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.state = Animation.STARTED
        
    def update(self):
        if self.state != Animation.STARTED:
            return
        instant = pygame.time.get_ticks() - self.start_time
        ratio = instant / float(self.duration)
        if ratio > 1:
            self.onEnd()
            self.state = Animation.ENDED
        else:    
            #insert interpolatio
            ratio = float((math.cos((ratio + 1) * math.pi) / 2.0) + 0.5);
            value = self.start_value + (self.end_value - self.start_value) * ratio
            self.onTick(value)
        
        
    def onTick(self, value):
        pass #to be overridden
    
    def onEnd(self):
        pass #to be overridden