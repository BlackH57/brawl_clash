from src import Entity
import properties as ppt


class Mob(Entity.Entity):
    def __init__(self, health, speed, x, y, size, sprite):
        super().__init__(health, speed, x, y, size, 1, sprite)
        ppt.sprites_mob.add(self)


class Slime(Mob):
    def __init__(self, x, y):
        super().__init__(10, 2, x, y, 1, "src/Sprites/Monsters/Slime.png")


class Coffre(Mob):
    def __init__(self, x, y):
        super().__init__(20, 5, x, y, 1, "src/Sprites/Monsters/Coffre.png")


class Lynx(Mob):
    def __init__(self, x, y):
        super().__init__(30, 10, x, y, 1.5, "src/Sprites/Monsters/Lynx.png")


class Robot(Mob):
    def __init__(self, x, y):
        super().__init__(40, 5, x, y, 1.5, "src/Sprites/Monsters/Robot.png")


class Kangoo(Mob):
    def __init__(self, x, y):
        super().__init__(20, 20, x, y, 1, "src/Sprites/Monsters/Kangoo.png")


class Larve(Mob):
    def __init__(self, x, y):
        super().__init__(10, 2, x, y, 1, "src/Sprites/Monsters/Larve.png")
