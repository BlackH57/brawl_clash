from src import Entity
import properties as ppt


class Player(Entity.Entity):
    def __init__(self, health, speed, jumpAcc, x, y, bag_max):
        self.weapon = None

        super().__init__(health, speed, jumpAcc, x, y, 1.5, bag_max, "Sprites/Soldat.png")

        ppt.all_moving_sprites.remove(self)
