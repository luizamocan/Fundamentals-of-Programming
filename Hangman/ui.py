from repository import TextFileRepository
from services import Services

class UI:
    def __init__(self, services):
        self.services = services

    @staticmethod
    def display_menu():
        print("1. Add a sentence")
        print("2. Start the game")
        print("0. Exit")

    def menu(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "0":
                break

            elif choice == "1":
                sentence = input("Enter your sentence: ")
                self.services.add_sentence(sentence)

            elif choice == "2":
                if self.services.start_game():
                    print(f"Output: \"{self.services.display_sentence}\" - \"{self.services.display_hangman}\"")
                    while not self.services.game_over():
                        guess = input("Enter your guess: ").lower()
                        display, hangman = self.services.play_round(guess)
                        print(f"Output: \"{display}\" - \"{hangman}\"")
                    if self.services.has_won():
                        print("YOU WON!")
                    else:
                        print("YOU LOST!")

            else:
                print("Invalid choice. Please try again.")

def main():
    repo = TextFileRepository("sentences.txt")
    services = Services(repo)
    ui = UI(services)
    ui.menu()

if __name__ == "__main__":
    main()
