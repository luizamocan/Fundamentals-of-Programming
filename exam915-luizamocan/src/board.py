import random
from texttable import Texttable


class Game:
    def __init__(self):
        self.grid_size = 7
        self.grid = [[" " for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.grid[3][3] = "E"
        self.attempts = 0
        self.destroyed = 0
        self.asteroids = self.place_asteroids()
        self.aliens = self.place_aliens()

    @staticmethod
    def is_valid_asteroid_placement( x, y, asteroid_positions):
        if (x, y) == (3, 3):
            return False
        for position1, position2 in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if (x + position1, y + position2) in asteroid_positions:
                return False
        return True

    def place_asteroids(self):
        asteroids = set()
        while len(asteroids) < 8:
            x, y = random.randint(0, 6), random.randint(0, 6)
            if self.is_valid_asteroid_placement(x, y, asteroids):
                asteroids.add((x, y))
                self.grid[x][y] = "*"
        return asteroids

    def is_valid_alien_placement(self, x, y, alien_positions):

        if (x, y) in self.asteroids or (x, y) == (3, 3):
            return False
        if abs(x - 3) + abs(y - 3) < 3:
            return False
        return (x, y) not in alien_positions

    def place_aliens(self):
        aliens = set()
        valid_positions = [
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
            (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
            (1, 6), (2, 6), (3, 6), (4, 6), (5, 6)
        ]

        while len(aliens) < 2:
            x, y = random.choice(valid_positions)
            if self.is_valid_alien_placement(x, y, aliens):
                aliens.add((x, y))
        return aliens

    def display_grid(self, reveal_aliens=False):
        table = Texttable()
        table.header([" "] + list("ABCDEFG"))


        for i, row in enumerate(self.grid):
            display_row = []
            for j, cell in enumerate(row):
                if (i, j) in self.aliens and reveal_aliens:
                    display_row.append("X")
                elif (i, j) in self.aliens:
                    display_row.append(" ")
                else:
                    display_row.append(cell)
            table.add_row([i + 1] + display_row)

        print(table.draw())


