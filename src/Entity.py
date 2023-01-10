from src import Bag
import pygame as pg


class Entity(pg.sprite.Sprite):

    def __init__(self, health: int, speed: int, x: int, y: int, bag_max: int, sprite: str):
        pg.sprite.Sprite.__init__(self)

        self.health = health
        self.walkingSpeed = speed
        self.runningSpeed = speed * 2

        self.speed = speed

        self.x = x
        self.y = y
        self.bag = Bag.Bag(bag_max, [])

        self.image = pg.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_coord(self):
        return self.rect.x, self.rect.y

    def get_stats(self):
        return self.health, self.speed

    # Mouvement
    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_up(self):
        self.rect.y -= self.speed

    # Modificateur de vitesse
    def run(self):
        self.speed = self.runningSpeed

    def walk(self):
        self.speed = self.walkingSpeed