import pygame as pg


class Wall(pg.sprite.Sprite):

    def __init__(self, x: int, y: int):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y

        # Image
        self.image = pg.image.load("Sprites/Wall.png").convert_alpha()

        self.rect = self.image.get_rect()


