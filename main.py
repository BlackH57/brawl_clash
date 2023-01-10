import pygame as pg


pg.init()
screen = pg.DOUBLEBUF

launched = True

while launched :
    for event in pg.event.get():
        if event.type == pg.QUIT:
            launched = False
 