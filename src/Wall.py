from src import Obstacle


class Wall(Obstacle.Obstacle):

    def __init__(self, x: int, y: int):
        super().__init__(x, y, "Sprites/Wall.png")
