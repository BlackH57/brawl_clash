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
