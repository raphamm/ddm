import pygame
from pygame.locals import *

white = pygame.Color("white")

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ddm')
img_player = pygame.image.load('player.png')
img_player.set_colorkey(white)
img = pygame.image.load('room.jpg')
img_width = img.get_width()
img_height = img.get_height()

from ddm import Level, Player
lev = Level(size_max=21)
pl = Player()
x_min, x_max, y_min, y_max = lev.getBounds()
for x, y in lev.rooms:
    print(x, y)
    DISPLAYSURF.blit(img, (x * img_width - img_width * x_min, y * img_height - img_height * y_min))
DISPLAYSURF.blit(img_player, (pl.xy[0] * img_width - img_width * x_min, pl.xy[1] * img_height - img_height * y_min))
lev.draw()

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
