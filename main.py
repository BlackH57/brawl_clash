import pygame as pg
import pygame.time

from src import Player
from src import Wall
from src import Game
from src import Map
import properties as ppt


pg.init()

pg.display.set_caption("Brawl Clash")  # titre de la fenêtre de jeu

window_surface = pg.display.set_mode(ppt.resolution, pg.RESIZABLE)  # ouverture de la fenêtre + modes
fpsClock = pg.time.Clock()
# boucle pour garder la fenêtre ouverte tant qu'on appuie pas sur la croix
launched = True


player = Player.Player(100, 10, 400, 600, 10)
grid = Map.Map([
    ["W","W","W","W","W","W","W","W","W","W"],
    ["W","W","W","W","W","W","W","W","W","W"],
    ["W","W","W","W","W","W","W","W","W","W"],
    ["W","W","W","W","W","W","W","W","W","W"],
    ["W","W","W","W","W","W","W","W","W","W"],
    ["W","W","W","W","W","W","W","W","W","W"],
    ["W","W","W","W","W","W","W","W","W","W"],
    ["W","W","W","W","W","W","W","W","W","W"],
    ["W","W","W","W","W","W","W","W","W","W"],
    ["W","W","W","W","W","W","W","W","W","W"]
])

instance = Game.Game(grid, player)
wall1 = Wall.Wall(0, 0)

cpt = 0
while launched:

    # Affichage des elements:
    window_surface.fill(ppt.black_color)
    window_surface.blit(wall1.image, wall1.rect)
    window_surface.blit(player.image, player.rect)

    # Mise a jour de l'ecran
    pg.display.flip()
    fpsClock.tick(ppt.FPS)

    # Mouvement
    if instance.keypressed.get(pg.K_q):
        print("Move left")
        player.move_left()
    if instance.keypressed.get(pg.K_d):
        print("Move right")
        player.move_right()
    if instance.keypressed.get(pg.K_z):
        print("Move up")
        player.move_up()
    if instance.keypressed.get(pg.K_s):
        print("Move down")
        player.move_down()

    # Gestion des evenements pygame
    for event in pg.event.get():
        print(event)

        if event.type == pg.QUIT:
            launched = False

        if event.type == pg.KEYDOWN:
            # Si MAJ enfoncé on cours
            if event.key == pg.K_LSHIFT:
                player.run()

        if event.type == pg.KEYUP:
            # Si on n'appuie plus sur MAJ ne cours plus
            if event.key == pg.K_LSHIFT:
                player.walk()

        # Enregistrement des touches actives
        if event.type == pg.KEYDOWN:
            instance.keypressed[event.key] = True
        if event.type == pg.KEYUP:
            instance.keypressed[event.key] = False


