from src import Obstacle
import properties as ppt

class Ladder(Obstacle.Obstacle):

    def __init__(self, x: int, y: int):
        super().__init__(x, y, "Sprites/Ladder.png")
        ppt.sprites_ladder.add(self)

        
