from src import Entity
import properties as ppt


class Mob(Entity.Entity):
    def __init__(self, health, speed, jumpAcc, x, y, size, sprite):
        super().__init__(health, speed, jumpAcc, x, y, size, 1, sprite)
        ppt.sprites_mob.add(self)


class Slime(Mob):
    def __init__(self, x, y):
        super().__init__(10, 2, 0, x, y, 1, "Sprites/Monsters/Slime.png")


class Coffre(Mob):
    def __init__(self, x, y):
        super().__init__(20, 5, 10, x, y, 1, "Sprites/Monsters/Coffre.png")


class Lynx(Mob):
    def __init__(self, x, y):
        super().__init__(30, 10, 20, x, y, 1, "Sprites/Monsters/Lynx.png")


class Robot(Mob):
    def __init__(self, x, y):
        super().__init__(40, 5, 10, x, y, 1, "Sprites/Monsters/Robot.png")


class Kangoo(Mob):
    def __init__(self, x, y):
        super().__init__(20, 20, 40, x, y, 1, "Sprites/Monsters/Kangoo.png")


class Larve(Mob):
    def __init__(self, x, y):
        super().__init__(10, 2, 0, x, y, 1, "Sprites/Monsters/Larve.png")
