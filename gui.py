import pygame
from pygame.locals import *
import sys

white = pygame.Color("white")
black = pygame.Color("black")
gray = pygame.Color("gray")

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ddm')
img_player = pygame.image.load('player.png')
img_player.set_colorkey(white)
img_room = pygame.image.load('room.jpg')
img_width = img_room.get_width()
img_height = img_room.get_height()
img_exit = pygame.image.load('stairs_down.png')
img_exit.set_colorkey(white)
img_wall = pygame.image.load('wall.png')


from ddm import Level, Player
lev = Level(size_max=21)
pl = Player()
x_min, x_max, y_min, y_max = lev.getBounds()
lev.draw()


def coords_map2pixel(x, y):
    """
    converts map coordinates to pixel coordinates in window.
    """
    x = x * img_width
    y = y * img_height
    return (x, y)


while True: # main game loop
    DISPLAYSURF.fill(gray)
    for x, y in lev.visited_rooms:
        DISPLAYSURF.blit(img_room, coords_map2pixel(x - pl.xy[0] + 5, y - pl.xy[1] + 5))
    if lev.exit in lev.visited_rooms:
        DISPLAYSURF.blit(img_exit, coords_map2pixel(lev.exit[0] - pl.xy[0] + 5, lev.exit[1] - pl.xy[1] + 5))
    DISPLAYSURF.blit(img_player, coords_map2pixel(pl.xy[0] - pl.xy[0] + 5, pl.xy[1] - pl.xy[1] + 5))
    for x, y in lev.visited_walls:
        DISPLAYSURF.blit(img_wall, coords_map2pixel(x - pl.xy[0] + 5, y - pl.xy[1] + 5)) 
        
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
                    lev.look_ahead(x, y)
            # player wants to exit
            elif event.key == K_RETURN:
                if lev.isExit(x, y):
                    lev = Level(size_max=21)
                    pl.xy = (0, 0)
                    x_min, x_max, y_min, y_max = lev.getBounds()
    pygame.display.update()
