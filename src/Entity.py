from src import Bag
import pygame as pg


class Entity(pg.sprite.Sprite):

    def __init__(self, health: int, speed: int, coords: (int, int), bag_max: int, sprite: str):
        pg.sprite.Sprite.__init__(self)

        self.health = health
        self.speed = speed
        self.sprite = sprite  # En vrai doit contenir l'image

        self.x = coords[0]
        self.y = coords[1]
        self.bag = Bag.Bag(bag_max, [])


    def get_coord(self):
        return self.x, self.y

    def get_stats(self):
        return self.health, self.speed
