import properties as ppt

class Game:
    def __init__(self, grid, player):
        self.grid = grid
        self.keypressed = {}
        self.player = player
        self.sprites = [wall for wall in grid.walls]

        block_size = ppt.resolution[1] / len(self.grid.map)
        self.player.rescale(block_size)

        player.speed = int(player.speed*block_size/100)
        player.walkingSpeed = int(player.walkingSpeed*block_size/100)
        player.runningSpeed = int(player.runningSpeed*block_size/100)
        player.jumpAcceleration = int(player.jumpAcceleration*block_size/100)



