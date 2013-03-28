import pygame
from pygame.locals import *
import sys

white = pygame.Color("white")
black = pygame.Color("black")

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ddm')
img_player = pygame.image.load('player.png')
img_player.set_colorkey(white)
img = pygame.image.load('room.jpg')
img_width = img.get_width()
img_height = img.get_height()
img_exit = pygame.image.load('stairs_down.png')
img_exit.set_colorkey(white)


from ddm import Level, Player
lev = Level(size_max=21)
pl = Player()
x_min, x_max, y_min, y_max = lev.getBounds()
lev.draw()

while True: # main game loop
    DISPLAYSURF.fill(black)
    for x, y in lev.rooms:
        DISPLAYSURF.blit(img, (x * img_width - img_width * x_min, y * img_height - img_height * y_min))
    DISPLAYSURF.blit(img_exit, (lev.exit[0] * img_width - img_width * x_min, lev.exit[1] * img_height - img_height * y_min))
    DISPLAYSURF.blit(img_player, (pl.xy[0] * img_width - img_width * x_min, pl.xy[1] * img_height - img_height * y_min))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # a key was pressed
        elif event.type == KEYDOWN:
            x, y = pl.xy
            # player movement
            if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                if event.key == K_LEFT:
                    x -= 1
                elif event.key == K_RIGHT:
                    x += 1
                elif event.key == K_UP:
                    y -= 1
                elif event.key == K_DOWN:
                    y += 1
                if lev.isRoom(x, y):
                    pl.xy = (x, y)
            # player wants to exit
            elif event.key == K_RETURN:
                if lev.isExit(x, y):
                    lev = Level(size_max=21)
                    pl.xy = (0, 0)
                    x_min, x_max, y_min, y_max = lev.getBounds()
    pygame.display.update()
