from src import Barrier


class Wall(Barrier.Barrier):

    def __init__(self, x: int, y: int):
        super().__init__(x, y, "Sprites/Wall.png")
        
