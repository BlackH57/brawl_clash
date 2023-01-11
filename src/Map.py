import pygame as pg
import properties as ppt
from src import Wall


class Map:
    def __init__(self, list_case: list[list[str]]):
        # W : Wall
        # space : Nothing
        self.map = list_case
        self.height = len(self.map)  # Recupere le nombre de block de hauteur
        self.walls = []

    def create_elements(self):
        size_block = ppt.resolution[1] / self.height

        # Dessinons la grille
        for j, colonne in enumerate(self.map):
            for i, block in enumerate(colonne):
                if block == "W":
                    wall = Wall.Wall(i * size_block, j * size_block)
                    wall.rescale(size_block)
                    self.walls.append(wall)
                    ppt.sprites_wall.add(wall)
                    ppt.all_moving_sprites.add(wall)
