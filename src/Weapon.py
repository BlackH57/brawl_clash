from src import Object
from src import Projectile
import pygame as pg


class Weapon(pg.sprite.Sprite):

    def __init__(self, fire_rate: int, damage: int, magazine: int, sprite):
        pg.sprite.Sprite.__init__(self)

        self.fire_rate = fire_rate
        self.damage = damage
        self.magazine = magazine

        # Image
        self.image = pg.image.load("Sprites/shotgun.png").convert_alpha()
        self.rect = self.image.get_rect()
