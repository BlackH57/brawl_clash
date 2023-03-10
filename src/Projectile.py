from src import Object
import properties as ppt
import pygame as pg


class Projectile(pg.sprite.Sprite):

    def __init__(self, x: int, y: int, dir_x: int, dir_y: int, speed: int, damage: int, sprite):
        print("Je suis créé")
        pg.sprite.Sprite.__init__(self)
        
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.speed = speed
        self.damage = damage

        # Image
        self.image = pg.image.load("Sprites/bullet.png").convert_alpha()
        self.image = pg.transform.scale(self.image, (10, 10))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        ppt.sprites_bullet.add(self)
        ppt.all_moving_sprites.add(self)

    def move(self):
        self.rect.x += (self.speed * self.dir_x)
        self.rect.y += (self.speed * self.dir_y)

    def hit(self):
        if pg.sprite.spritecollide(self, ppt.sprites_wall, False):
            ppt.sprites_bullet.remove(self)
            ppt.all_moving_sprites.remove(self)
        for sprite in pg.sprite.spritecollide(self, ppt.sprites_mob, False):    # True temporaire
            # Supprime le sprite de la balle
            ppt.sprites_bullet.remove(self)
            ppt.all_moving_sprites.remove(self)

            # Fait des degats aux monstres
            sprite.hurt(self.damage)


            # mettre des degats
