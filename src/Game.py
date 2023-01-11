class Game:
    def __init__(self, grid, player):
        self.grid = grid
        self.keypressed = {}
        self.player = player
        self.sprites = [wall for wall in grid.walls]




