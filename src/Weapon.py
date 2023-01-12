from src import Object
import pygame as pg

class Weapon(pg.sprite.Sprite):

    def __init__(self, x: int, y: int, sprite):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        # Image
        self.image = pg.image.load(sprite).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    #def shoot():
        