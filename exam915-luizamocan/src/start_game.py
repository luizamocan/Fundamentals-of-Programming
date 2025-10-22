
class StartGame:
    def __init__(self, repository):

        self.game = repository
        self.fired_positions = set()

    def fire(self, coordinate):
        """
        The function fires if the coordinates are valid(are in the matrix,were not fired at,are not asteroids ) ,
         replaces the empty square with a '-' and displayed the game
        :param coordinate: the coordinates of the square we want to fire
        :return: ValueError or IndexError if the coordinates are invalid
        returns a message if the coordinates are valid, but not appropriate to the task(already fired,asteroid)
        """
        try:
            col = ord(coordinate[0].upper()) - ord("A")
            row = int(coordinate[1]) - 1
            if not (0 <= row < self.game.grid_size and 0 <= col < self.game.grid_size):
                raise ValueError
        except (IndexError, ValueError):
            print("Invalid input!")
            return

        if (row, col) in self.fired_positions:
            print("You already fired at this square! Try again.")
            return

        self.fired_positions.add((row, col))
        if (row, col) in self.game.asteroids:
            print(f"You hit an asteroid at {coordinate.upper()}! Nothing happens.")
            return

        if (row, col) in self.game.aliens:
            print(f"Direct hit! You destroyed an alien ship at {coordinate.upper()}!")
            self.game.aliens.remove((row, col))
            self.game.destroyed += 1
            self.game.grid[row][col] = "-"
        else:
            print(f"Miss!")
            self.game.grid[row][col] = "-"

        self.game.display_grid()
        if self.game.destroyed == 2:
            print("You won the game!")




