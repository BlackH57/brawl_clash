from src import Obstacle


class Ladder(Obstacle.Obstacle):

    def __init__(self, x: int, y: int):
        super().__init__(x, y, "Sprites/Ladder.png")
        

        
