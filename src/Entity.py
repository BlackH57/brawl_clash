from src import Bag
import pygame as pg
import properties as ppt


class Entity(pg.sprite.Sprite):

    def __init__(self, health: int, speed: int, x: int, y: int, bag_max: int, sprite: str):
        """
        :param health: Vie initiale de l'entité
        :param speed: Vitesse
        :param x: Positionnement horizontal
        :param y: Positionnement vertical
        :param bag_max: Capacite max du sac
        :param sprite: Chemin de l'image dans le dossier
        """
        pg.sprite.Sprite.__init__(self)

        # Statistique de base
        self.max_health = health
        self.health = health
        self.speed = speed

        # Statistique de vitesse a terre
        self.walkingSpeed = speed
        self.runningSpeed = speed * 3/2

        # Statistique de vitesse aerienne
        self.jumpAcceleration = 30
        self.jumpSpeed = 0

        # Dis si l'entite est dans les airs
        self.falling = True

        # Inventaire
        self.bag = Bag.Bag(bag_max, [])

        # Image
        self.image = pg.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Ajout du sprite dans des groupes
        ppt.sprites_entity.add(self)
        ppt.all_moving_sprites.add(self)

    def get_coord(self):
        """
        :return: Coordonnees du joueur
        """
        return self.rect.x, self.rect.y

    def get_stats(self):
        return self.health, self.speed

    # Mouvement
    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def jump(self):
        if not self.isFalling():
            self.jumpSpeed = self.jumpAcceleration

    # Modificateur de vitesse
    def run(self):
        self.speed = self.runningSpeed

    def walk(self):
        self.speed = self.walkingSpeed

    def isFalling(self):
        if self.jumpSpeed > 0:
            return True

        self.move_down()
        fall = False
        if len(pg.sprite.spritecollide(self, ppt.sprites_wall, False)) == 0:
            fall = True
        self.move_up()

        return fall

    def fall_update(self):
        # On regarde si on tombe
        if self.isFalling():
            self.rect.y -= self.jumpSpeed
            self.jumpSpeed -= 2
            colliding_sprites = pg.sprite.spritecollide(self, ppt.sprites_wall, False)
            if colliding_sprites:
                if self.jumpSpeed > 0:
                    self.rect.top = colliding_sprites[0].rect.bottom
                elif self.jumpSpeed < 0:
                    self.rect.bottom = colliding_sprites[0].rect.top
                self.jumpSpeed = 0
