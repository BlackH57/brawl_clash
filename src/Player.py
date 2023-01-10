from src import Entity


class Player(Entity.Entity):
    def __init__(self, health, speed, x, y, bag_max):
        self.weapon = None

        super().__init__(health, speed, x, y, bag_max, "Sprites/Soldat.png")

        
