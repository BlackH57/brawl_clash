from src import Object
import pygame as pg

class Projectile(pg.sprite.Sprite):

    def __init__(self, x: int, y: int, dir_x: int, dir_y: int, speed: int, dmg: int, sprite):
        pg.sprite.Sprite.__init__(self)
        
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.speed = speed
        self.dmg = dmg

        # Image
        self.image = pg.image.load("Sprites/Ladder.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def move(self):
        self.rect.x += (self.speed * self.dir_x)
        self.rect.y += (self.speed * self.dir_y)