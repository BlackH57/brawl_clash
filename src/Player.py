from src import Entity
from src import Projectile
from src import Weapon
import properties as ppt


class Player(Entity.Entity):
    def __init__(self, weapon):
        self.weapon = weapon
        super().__init__(100, 10, 30, 400, 500, 1.5, 10, "Sprites/Soldat.png")
        ppt.all_moving_sprites.remove(self)

    def shoot(self, dir_x: int, dir_y: int):
        Projectile.Projectile(self.rect.midright[0], self.rect.midright[1], dir_x, dir_y, 10, self.weapon.dmg, "Sprites/bullet.png")

