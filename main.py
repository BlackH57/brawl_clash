import pygame as pg
from src import Player
from src import Wall


resolution = (1280, 800)  # résolution de l'écran
pg.init()

pg.display.set_caption("Brawl Clash")  # titre de la fenêtre de jeu

window_surface = pg.display.set_mode(resolution, pg.RESIZABLE)  # ouverture de la fenêtre + modes

# boucle pour garder la fenêtre ouverte tant qu'on appuie pas sur la croix
launched = True

player = Player.Player(100, 10, 400, 600)

wall1 = Wall.Wall(0, 0)

while launched:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            launched = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LSHIFT:
                player.speed = 50

    # Affichage des elements:
    window_surface.blit(wall1.image, (wall1.x, wall1.y))
    window_surface.blit(player.image, (player.x, player.y))

    # Actualisation de l'image
    pg.display.flip()
