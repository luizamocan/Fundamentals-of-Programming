import pickle
from src.domain import Student

class MemoryRepository:
    def __init__(self):
        self._students = []

    def add(self, student):
        self._students.append(student)

    def get_all(self):
        return self._students

    def remove_by_group(self, group):
        self._students = [student for student in self._students if student.group != group]

    def clear(self):
        self._students = []

class TextFileRepository(MemoryRepository):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self._load()

    def _load(self):
        try:
            with open(self.file_name, "r") as file:
                for line in file:
                    student_id, name, group = line.strip().split(", ")
                    self.add(Student(int(student_id), name, int(group)))
        except FileNotFoundError:
            pass

    def _save(self):
        with open(self.file_name, "w") as file:
            for student in self._students:
                file.write(f"{student.student_id}, {student.name}, {student.group}\n")

    def add(self, student):
        super().add(student)
        self._save()

    def remove_by_group(self, group):
        super().remove_by_group(group)
        self._save()

    def clear(self):
        super().clear()
        with open(self.file_name, "w") as file:
            pass

class BinaryFileRepository(MemoryRepository):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name
        self._load()

    def _load(self):
        try:
            with open(self.file_name, "rb") as file:
                self._students = pickle.load(file)
        except FileNotFoundError:
            self._students=[]
        except EOFError:
            self._students=[]

    def _save(self):
        with open(self.file_name, "wb") as file:
            pickle.dump(self._students, file)

    def add(self, student):
        super().add(student)
        self._save()

    def remove_by_group(self, group):
        super().remove_by_group(group)
        self._save()



