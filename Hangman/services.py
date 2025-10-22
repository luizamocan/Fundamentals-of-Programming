import random

class Services:
    def __init__(self, repository):
        self.repository = repository
        self.selected_sentence = ""
        self.display_sentence = ""
        self.display_hangman = ""
        self.guessed_letters = set()
        self.sentences=[]

    def add_sentence(self, sentence):
        """
        The function adds a sentence to the list of sentences if it has at least one word and
        all of them have at least 3 letters
        :param sentence: the sentence to be added
        """
        words = sentence.split()
        if len(words) > 0 and all(len(word) >= 3 for word in words):
            self.repository.save_sentence(sentence)

    def start_game(self):
        self.sentences = self.repository.get_sentences()
        if not self.sentences:
            print("No sentences found")
            return False

        self.selected_sentence = random.choice(self.sentences)
        self.display_hangman = ""
        self.guessed_letters.clear()
        self.display_sentence = self.mask_sentence(self.selected_sentence)
        return True

    @staticmethod
    def mask_sentence(sentence):
        masked = []

        for word in sentence.split():
            if len(word) <= 2:
                masked_word = word
            else:
                masked_word = word[0] + "_" * (len(word) - 2) + word[-1]
            masked.append(masked_word)
        return " ".join(masked)

    def play_round(self, letter):
        if letter in self.guessed_letters:
            return self.display_sentence, self.display_hangman

        self.guessed_letters.add(letter)
        if letter in self.selected_sentence:
            words = self.selected_sentence.split()
            masked_words = []
            for word in words:
                if len(word) <= 2:
                    masked_words.append(word)
                else:
                    masked_word = word[0] + "".join(
                        c if c in self.guessed_letters else "_"
                        for c in word[1:-1]) + word[-1]
                    masked_words.append(masked_word)
            self.display_sentence = " ".join(masked_words)
        else:
            self.display_hangman = "hangman"[:len(self.display_hangman) + 1]

        return self.display_sentence, self.display_hangman

    def game_over(self):
        return self.display_sentence.replace(" ", "") == self.selected_sentence.replace(" ", "") or self.display_hangman == "hangman"

    def has_won(self):
        return self.display_sentence.replace(" ", "") == self.selected_sentence.replace(" ", "")
