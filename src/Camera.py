import properties as ppt
import pygame as pg


class Camera:
    def __init__(self, game):
        self.game = game

    def move_right(self, dist=None):
        dist_used = self.game.player.speed
        if dist is not None:
            dist_used = dist
        for sprite in ppt.all_moving_sprites.sprites():
            sprite.rect.x -= dist_used

    def move_left(self, dist=None):
        dist_used = self.game.player.speed
        if dist is not None:
            dist_used = dist
        for sprite in ppt.all_moving_sprites.sprites():
            sprite.rect.x += dist_used

    def move_up(self, dist=None):
        dist_used = self.game.player.speed
        if dist is not None:
            dist_used = dist
        for sprite in ppt.all_moving_sprites.sprites():
            sprite.rect.y += dist_used

    def move_down(self, dist=None):
        dist_used = self.game.player.speed
        if dist is not None:
            dist_used = dist
        for sprite in ppt.all_moving_sprites.sprites():
            sprite.rect.y -= dist_used

    # Combinaison des methodes plus hauts
    def move(self):
        if self.game.keypressed.get(pg.K_q):
            self.move_left()
            for sprite in pg.sprite.spritecollide(self.game.player, ppt.sprites_wall, False):
                if sprite.rect.right - self.game.player.rect.left >= 0:
                    self.move_right(sprite.rect.right - self.game.player.rect.left)
                    break

        if self.game.keypressed.get(pg.K_d):
            self.move_right()
            for sprite in pg.sprite.spritecollide(self.game.player, ppt.sprites_wall, False):
                if sprite.rect.left - self.game.player.rect.right <= 0:
                    self.move_left(self.game.player.rect.right - sprite.rect.left)
                    break

    def climb(self):
        if len(pg.sprite.spritecollide(self.game.player, ppt.sprites_ladder, False)) != 0:
            self.game.player.jumpSpeed = 0 
            if self.game.keypressed.get(pg.K_z):
                self.move_up()

            if self.game.keypressed.get(pg.K_s):
                self.move_down()
