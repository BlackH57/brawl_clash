from Entity import Entity


class Player(Entity):
    def __init__(self, health, speed, coords, bag_max, sprite):
        self.weapon = None

        super().__init__(health, speed, coords, bag_max, sprite)
