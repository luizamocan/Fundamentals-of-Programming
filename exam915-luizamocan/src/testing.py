from start_game import StartGame


class MockGame:
    def __init__(self):
        self.grid_size = 5
        self.grid = [['-' for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.asteroids = {(0, 0), (1, 1)}
        self.aliens = {(2, 2), (3, 3)}
        self.destroyed = 0

    def display_grid(self, reveal_aliens=False):
        pass


class TestFireFunction:
    def __init__(self):
        self.mock_game = MockGame()
        self.start_game = StartGame(self.mock_game)

    def test_fire(self):
        assert self.start_game.fire("A1") is None
        assert self.start_game.fire("C3") is None
        assert self.start_game.fire("E5") is None
        assert self.start_game.fire("C3") is  None



def main():
    tests = TestFireFunction()
    tests.test_fire()


if __name__ == "__main__":
    main()
