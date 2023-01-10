import pygame as pg

resolution = (1280, 800) #résolution de l'écran
pg.init() 

pg.display.set_caption("Brawl Clash") #titre de la fenêtre de jeu

window_surface = pg.display.set_mode(resolution, pg.RESIZABLE) #ouverture de la fenêtre + modes

#boucle pour garder la fenêtre ouverte tant qu'on appuie pas sur la croix
launched = True
while launched :
    for event in pg.event.get():
        if event.type == pg.QUIT:
            launched = False
 