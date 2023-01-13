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
                position = (i+4) * size_block, j * size_block
                # Mur
                if block == "W":
                    wall = Wall.Wall(position[0], position[1])
                    wall.rescale(size_block)
                    self.walls.append(wall)


                # Echelle
                elif block == "L":
                    ladder = Ladder.Ladder(position[0], position[1])
                    ladder.rescale(size_block)

                # Joueur
                # elif block == "P":

                # Slime / Blob
                elif block == "B":
                    print("Blob")
                    blob = Mob.Slime(position[0], position[1])
                    blob.rescale(size_block)

                # Coffre
                elif block == "C":
                    print("Coffre")
                    coffre = Mob.Coffre(position[0], position[1])
                    coffre.rescale(size_block)

                # Lynx
                elif block == "X":
                    print("Lynx")
                    lynx = Mob.Lynx(position[0], position[1])
                    lynx.rescale(size_block)

                # Robot
                elif block == "R":
                    print("Robot")
                    robot = Mob.Robot(position[0], position[1])
                    robot.rescale(size_block)

                # Kangoo
                elif block == "K":
                    print("Kangoo")
                    kangoo = Mob.Kangoo(position[0], position[1])
                    kangoo.rescale(size_block)

                # Larve / Slug
                elif block == "S":
                    print("Larve")
                    larve = Mob.Larve(position[0], position[1])
                    larve.rescale(size_block)
