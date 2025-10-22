from board import Game
from start_game import StartGame


class UI:
    def __init__(self):
        self.game_instance = None
        self.start_game = None

    @staticmethod
    def print_menu():
        print("1. Start the game")
        print("2. Attack a square")
        print("3. Reveal alien ships")
        print("0. Exit")

    def menu(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")

            if choice == "0":
                break

            elif choice == "1":
                self.game_instance = Game()
                self.start_game = StartGame(self.game_instance)
                self.game_instance.display_grid()

            elif choice == "2":
                while True:
                    coordinate = input("Enter the coordinates to fire:  ")
                    if coordinate.lower() == "quit":
                        break
                    self.start_game.fire(coordinate)

                    if self.game_instance.destroyed == 2:
                        break

            elif choice == "3":
                self.game_instance.display_grid(reveal_aliens=True)

            else:
                print("Invalid choice. Please try again.")

def main():
    ui = UI()
    ui.menu()

if __name__ == '__main__':
    main()