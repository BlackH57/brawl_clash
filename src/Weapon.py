from src import Object
from src import Projectile
import pygame as pg

class Weapon(pg.sprite.Sprite):

    def __init__(self, fire_rate: int, dmg: int, magazine: int, sprite):
        pg.sprite.Sprite.__init__(self)

        self.fire_rate = fire_rate
        self.dmg = dmg
        self.magazine = magazine

        # Image
        self.image = pg.image.load("Sprites/shotgun.png").convert_alpha()
        self.rect = self.image.get_rect()
        
    
    def shoot(self, dir_x: int, dir_y: int):
        bullet = Projectile.Projectile(self.rect.centerx, self.rect.centery, dir_x, dir_y, 10, self.dmg, "Sprites/bullet.png")

    


        