import pygame
from pygame.locals import *


pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ddm')
img = pygame.image.load('room.jpg')
img_width = img.get_width()
img_height = img.get_height()

from ddm import Level
lev = Level(size_max=21)
x_min, x_max, y_min, y_max = lev.getBounds()
for x, y in lev.rooms:
    print(x, y)
    DISPLAYSURF.blit(img, (x * img_width - img_width * x_min, y * img_height - img_height * y_min))
lev.draw()

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
