import pygame as pg


class Wall(pg.sprite.Sprite):

    def __init__(self, x: int, y: int, width: int, height: int, sprite: str, color):
        pg.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.sprite = sprite  # Doit contenir l'image en vrai


        # Image
        self.image, self.rect = pg.image.load("../Sprites/Wall.png")

        self.rect = self.image.get_rect()

