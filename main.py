import math
import pygame
import pygame as pg
from src import Player
from src import Game
from src import Map
from src import Camera
from src import Weapon

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
player = Player.Player(Weapon.Weapon(1.5, 20, 30, "Sprites/shotgun.png"))
grid = Map.Map([
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "L"," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "L"," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "L"," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W", "W", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", "L", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", "L", "W", "W", " ", " ", " ", " ", " ", "W", "W", " ", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", "L", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "W", " ", " ", " ", " ", " ", " "," ", " ", " ", "S", " ", " "," ", " ", " ", " ", " ", " ", " ", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W","W", "W", "W", "W", "W", "W","W", "W", "W", "W", "W", "W", "W", "W"]
])

grid.create_elements()

game = Game.Game(grid, player)

camera = Camera.Camera(game)

# boucle pour garder la fenêtre ouverte tant qu'on appuie pas sur la croix
launched = True

while launched:
    # Affichage des elements :
    # Fond
    window_surface.fill(ppt.black_color)

    # Murs
    for wall in ppt.sprites_wall:
        if wall in ppt.all_moving_sprites:
            window_surface.blit(wall.image, wall.rect)

    # Echelles
    for ladder in ppt.sprites_ladder:
        if ladder in ppt.all_moving_sprites:
            window_surface.blit(ladder.image, ladder.rect)

    # Joueur
    game.player.fall_update()
    window_surface.blit(player.image, player.rect)

    # Balles
    for bullet in ppt.sprites_bullet:
        window_surface.blit(bullet.image, bullet.rect)
        bullet.move()
        bullet.hit()
    
    # Mouvement
    camera.move()

    # Mise a jour de l'ecran
    pg.display.flip()
    fpsClock.tick(ppt.FPS)

    # Gestion des evenements pygame
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            launched = False
            pygame.quit()

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

        # Utilisation d'arme
        if event.type == pg.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
            # verifier nbr balles
            #if player.weapon.magazine > 0:
                norme = math.sqrt( (pygame.mouse.get_pos()[0] - player.rect.x)**2 + (pygame.mouse.get_pos()[1] - player.rect.y)**2 )
                player.shoot((pygame.mouse.get_pos()[0] - player.rect.x)/norme, (pygame.mouse.get_pos()[1] - player.rect.y)/norme)
                

