from src import Bag


class Entity:

    def __init__(self, health: int, speed: int, x: int, y: int, bag_max: int, sprite: str):
        self.health = health
        self.speed = speed
        self.sprite = sprite    # En vrai doit contenir l'image

        self.x = x
        self.y = y
        self.bag = Bag.Bag(bag_max, [])

    def get_coord(self):
        return self.x, self.y

    def get_stats(self):
        return self.health, self.speed
