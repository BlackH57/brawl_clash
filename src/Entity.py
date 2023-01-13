from src import Bag
import pygame as pg
import properties as ppt


class Entity(pg.sprite.Sprite):

    def __init__(self, health: int, speed: int, jumpAcc: int, x: int, y: int, size: float, bag_max: int, sprite: str):
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
        self.size = size    # En nombre de block

        # Statistique de vitesse a terre
        self.walkingSpeed = speed
        self.runningSpeed = int(speed * 3 / 2)

        # Statistique de vitesse aerienne
        self.jumpAcceleration = jumpAcc
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

    # Recuperation des informations
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
        if not self.isFalling():  # and not pg.sprite.spritecollide(self, ppt.sprites_ladder, False):
            self.jumpSpeed = self.jumpAcceleration

    # Modificateur de vitesse
    def run(self):
        self.speed = self.runningSpeed

    def walk(self):
        self.speed = self.walkingSpeed

    def isFalling(self):
        if self.jumpSpeed > 0:
            return True

        if pg.sprite.spritecollide(self, ppt.sprites_ladder, False):
            return False

        self.move_down()

        collision = pg.sprite.spritecollide(self, ppt.sprites_wall, False)

        if not collision:
            self.move_up()
            return True

        else:
            self.rect.bottom = collision[0].rect.top
            return False

    def fall_update(self):
        # On regarde si on tombe
        if self.isFalling():
            self.rect.y -= self.jumpSpeed
            self.jumpSpeed -= 2
            colliding_sprites = pg.sprite.spritecollide(self, ppt.sprites_wall, False)
            if colliding_sprites:
                print(colliding_sprites)
                if self.jumpSpeed > 0:
                    self.rect.top = colliding_sprites[0].rect.bottom
                elif self.jumpSpeed < 0:
                    self.rect.bottom = colliding_sprites[0].rect.top
                self.jumpSpeed = 0

    # Convertisseur de taille
    def rescale(self, block_size):
        coord = self.rect.x, self.rect.y
        ratio = self.image.get_height()/self.image.get_width()
        self.image = pg.transform.scale(self.image, (self.size*block_size, self.size*block_size*ratio))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coord

    def hurt(self, damage):
        self.health -= damage

        # S'il n'a plus de vie il meurt
        if self.health < 0:
            ppt.all_moving_sprites.remove(self)
            ppt.sprites_mob.remove(self)
            ppt.sprites_entity.remove(self)
