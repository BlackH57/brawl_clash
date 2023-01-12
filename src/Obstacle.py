import pygame as pg
import properties as ppt

class Obstacle(pg.sprite.Sprite):

    def __init__(self, x: int, y: int, sprite):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        # Image
        self.image = pg.image.load(sprite).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        ppt.all_moving_sprites.add(self)

    def rescale(self, size):
        rect = self.rect.x, self.rect.y
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = rect
