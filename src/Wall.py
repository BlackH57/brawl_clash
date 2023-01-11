import pygame as pg


class Wall(pg.sprite.Sprite):

    def __init__(self, x: int, y: int):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        # Image
        self.image = pg.image.load("Sprites/Wall.png").convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def rescale(self, size):
        rect = self.rect.x, self.rect.y
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = rect
