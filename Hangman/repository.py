class TextFileRepository:
    def __init__(self, file_name):
        self.file_name = file_name
        self.sentences = self.load_sentences()

    def load_sentences(self):
        try:
            with open(self.file_name, "r") as file:
                sentences = [line.strip() for line in file if line.strip()]
                return sentences if len(sentences) >= 5 else []
        except FileNotFoundError:
            return []

    def save_sentence(self, sentence):

        """
        The function saves the sentence in the sentences list if it doesn't exist
        :param sentence: the sentence to be saved
        """
        if sentence not in self.sentences:
            self.sentences.append(sentence)
            with open(self.file_name, "a") as file:
                file.write(sentence + "\n")

    def get_sentences(self):
        return self.sentences
