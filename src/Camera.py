import properties as ppt
import pygame as pg

class Camera:
    def __init__(self, game):
        self.game = game

    def move_right(self):
        for sprite in ppt.all_moving_sprites.sprites():
            sprite.rect.x -= self.game.player.speed

    def move_left(self):
        for sprite in ppt.all_moving_sprites.sprites():
            sprite.rect.x += self.game.player.speed

    def move_up(self):
        for sprite in ppt.all_moving_sprites.sprites():
            sprite.rect.y += self.game.player.speed

    def move_down(self):
        for sprite in ppt.all_moving_sprites.sprites():
            sprite.rect.y -= self.game.player.speed

###################

    def climb(self):
        if len(pg.sprite.spritecollide(self.game.player, ppt.sprites_ladder, False)) != 0:
            self.game.player.jumpSpeed = 0 
            if self.game.keypressed.get(pg.K_z):
                self.move_up()

            if self.game.keypressed.get(pg.K_s):
                self.move_down()
