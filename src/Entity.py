from src import Bag
import pygame as pg


class Entity(pg.sprite.Sprite):

    def __init__(self, health: int, speed: int, x:int, y: int, bag_max: int, sprite: str):
        pg.sprite.Sprite.__init__(self)

        self.health = health
        self.speed = speed

        self.x = x
        self.y = y
        self.bag = Bag.Bag(bag_max, [])

        self.image = pg.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect()

    def get_coord(self):
        return self.rect.x, self.rect.y

    def get_stats(self):
        return self.health, self.speed
