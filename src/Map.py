import pygame as pg
import properties as ppt
from src import Wall
from src import Ladder
from src import Mob

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
                # Mur
                if block == "W":
                    wall = Wall.Wall(i * size_block, j * size_block)
                    wall.rescale(size_block)
                    self.walls.append(wall)


                # Echelle
                elif block == "L":
                    ladder = Ladder.Ladder(i * size_block, j * size_block)
                    ladder.rescale(size_block)

                # Joueur
                # elif block == "P":

                # Slime / Blob
                elif block == "B":
                    print("Blob")
                    blob = Mob.Slime(i * size_block, j * size_block)
                    blob.rescale(size_block)

                # Coffre
                elif block == "C":
                    print("Coffre")
                    coffre = Mob.Coffre(i * size_block, j * size_block)
                    coffre.rescale(size_block)

                # Lynx
                elif block == "X":
                    print("Lynx")
                    lynx = Mob.Lynx(i * size_block, j * size_block)
                    lynx.rescale(size_block)

                # Robot
                elif block == "R":
                    print("Robot")
                    robot = Mob.Robot(i * size_block, j * size_block)
                    robot.rescale(size_block)

                # Kangoo
                elif block == "K":
                    print("Kangoo")
                    kangoo = Mob.Kangoo(i * size_block, j * size_block)
                    kangoo.rescale(size_block)

                # Larve / Slug
                elif block == "S":
                    print("Larve")
                    larve = Mob.Larve(i * size_block, j * size_block)
                    larve.rescale(size_block)
