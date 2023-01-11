import pygame as pg
from src import Player
from src import Game
from src import Map
from src import Camera

import properties as ppt

# Initialisation des modules
pg.init()

# Titre de la fenêtre de jeu
pg.display.set_caption("Brawl Clash")

# Creation de la fenêtre + modes
window_surface = pg.display.set_mode(ppt.resolution, pg.RESIZABLE)

# Nombre d'images traitees par seconde
fpsClock = pg.time.Clock()

# Creation des elements du jeu
player = Player.Player(100, 10, 400, 600, 10)
grid = Map.Map([
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["W", " ", " ", " ", " ", " ", "W", "W", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["W", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["W", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["W", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"]
])

grid.create_elements()

game = Game.Game(grid, player)

camera = Camera.Camera(game)

# boucle pour garder la fenêtre ouverte tant qu'on appuie pas sur la croix
launched = True

while launched:
    # print(pg.sprite.spritecollide(game.player, ppt.sprites_wall, True))

    # Affichage des elements :
    # Fond
    window_surface.fill(ppt.black_color)

    # Murs
    for wall in ppt.sprites_wall:
        if wall in ppt.all_moving_sprites:
            window_surface.blit(wall.image, wall.rect)

    # Joueur
    player.height_update()
    window_surface.blit(player.image, player.rect)

    # Mise a jour de l'ecran
    pg.display.flip()
    fpsClock.tick(ppt.FPS)

    # Mouvement
    if game.keypressed.get(pg.K_q):
        camera.move_left()
        if len(pg.sprite.spritecollide(game.player, ppt.sprites_wall, False)) != 0:
            camera.move_right()

    if game.keypressed.get(pg.K_d):
        camera.move_right()
        if len(pg.sprite.spritecollide(game.player, ppt.sprites_wall, False)) != 0:
            camera.move_left()

    if game.keypressed.get(pg.K_z):
        camera.move_up()
        if len(pg.sprite.spritecollide(game.player, ppt.sprites_wall, False)) != 0:
            camera.move_down()

    if game.keypressed.get(pg.K_s):
        camera.move_down()
        if len(pg.sprite.spritecollide(game.player, ppt.sprites_wall, False)) != 0:
            camera.move_up()

    # Gestion des evenements pygame
    for event in pg.event.get():
        if event.type == pg.QUIT:
            launched = False

        # Enregistrement des touches actives
        if event.type == pg.KEYDOWN:
            game.keypressed[event.key] = True
        if event.type == pg.KEYUP:
            game.keypressed[event.key] = False

        if event.type == pg.KEYDOWN:
            # Si MAJ enfoncé on cours
            if event.key == pg.K_LSHIFT:
                player.run()

            if event.key == pg.K_SPACE:
                game.player.jump()

        if event.type == pg.KEYUP:
            # Si on n'appuie plus sur MAJ ne cours plus
            if event.key == pg.K_LSHIFT:
                player.walk()
