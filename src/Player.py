import utilities as ut
from src import Entity
from src import Projectile
import properties as ppt
import pygame as pg


class Player(Entity.Entity):
    def __init__(self, weapon):
        self.weapon = weapon
        super().__init__(100, 10, 30, 400, 500, 1.5, 10, "Sprites/Soldat.png")
        ppt.all_moving_sprites.remove(self)

    def shoot(self):
        # Position initiale du tir
        pos_init = self.rect.midright
        decalage_y = -15
        pos_init = pos_init[0], pos_init[1]+decalage_y

        # Position de la souris
        pos_mouse = pg.mouse.get_pos()

        # Direction
        dir_x = pos_mouse[0] - pos_init[0]
        dir_y = pos_mouse[1] - pos_init[1]

        # Normalisation du vecteur
        vect = ut.normalize_vec([dir_x, dir_y])

        # Creation du projectile
        Projectile.Projectile(pos_init[0], pos_init[1], vect[0], vect[1], 40, self.weapon.damage, "Sprites/bullet.png")

