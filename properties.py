import pygame as pg

# window_resolution = pg.get_size()

black_color = (0, 0, 0)  # Triplet RGB du noir
resolution = (1280, 800)  # résolution de l'écran
FPS = 60  # image par seconde


sprites_wall = pg.sprite.Group()
sprites_ladder = pg.sprite.Group()
sprites_entity = pg.sprite.Group()
all_moving_sprites = pg.sprite.Group()
