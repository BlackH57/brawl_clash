from src import Obstacle
import properties as ppt

class Wall(Obstacle.Obstacle):

    def __init__(self, x: int, y: int):
        super().__init__(x, y, "Sprites/Wall.png")
        ppt.sprites_wall.add(self)
