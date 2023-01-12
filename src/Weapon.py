from src import Object
from src import Projectile
import pygame as pg

class Weapon(pg.sprite.Sprite):

    def __init__(self, x: int, y: int, fire_rate: int, dmg: int, sprite):
        pg.sprite.Sprite.__init__(self)

        self.fire_rate = fire_rate
        self.dmg = dmg
        self.bullet = bullet


        # Image
        self.image = pg.image.load("Sprites/shotgun.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def shoot(self, dir_x: int, dir_y: int):
        bullet = Projectile.Projectile(self.rect.centerx, self.rect.centery, dir_x, dir_y, 10, self.dmg, "Sprites/bullet.png")
        bullet.move()




        