import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Hello World!')
done = False;
while not done: # main game loop
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            done = True
        else:
            print event
            pygame.display.update()
    pygame.event.pump()

pygame.quit()
sys.exit()
