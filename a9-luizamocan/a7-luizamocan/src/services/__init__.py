import random
from src.domain import Student

def generate_students(n):
    """
    Generate a list of students with unique IDs from 1 to 100,
    names chosen randomly from a predefined list, and groups randomly selected from 911 to 915.

    Args:
        n (int): The number of students to generate.

    Returns:
        list[Student]: List of generated Student objects.

    Raises:
        ValueError: If n exceeds the number of available unique IDs.
    """

    names = ["Ana", "Luiza", "Alex", "Vasile", "Cristian", "Alexia", "Mihai", "Carmen", "Adi","Alin", "Dacian"]
    group_range = range(911, 916)
    used_ids = set()
    students = []

    while len(students) < n:
        student_id = random.randint(1, 100)
        if student_id not in used_ids:  # Ensure unique ID
            used_ids.add(student_id)
            name = random.choice(names)
            group = random.choice(group_range)
            students.append(Student(student_id, name, group))

    return students


class Services:
    def __init__(self, repository):
            self._repository = repository
            self._undo_stack = []

    def add_student(self, student):
            # Check for duplicate ID
            for existing_student in self._repository.get_all():
                if existing_student.student_id == student.student_id:
                    raise ValueError(f"Student ID {student.student_id} already exists.")

            # Add student if ID is unique
            self._undo_stack.append(("remove", self._repository.get_all()))
            self._repository.add(student)

    def get_all_students(self):
        return self._repository.get_all()

    def remove_students_by_group(self, group):
        removed_students = [s for s in self._repository.get_all() if s.group == group]
        self._undo_stack.append(("add", self._repository.get_all()))
        self._repository.remove_by_group(group)

    def undo(self):
        if not self._undo_stack:
            raise Exception("No more operations to undo.")

        operation, previous_state = self._undo_stack.pop()
        self._repository.clear()

        if operation == "remove":
            for student in previous_state:
                self._repository.add(student)
            print("Undo: Students removed.")
        elif operation == "add":
            for student in previous_state:
                self._repository.add(student)
            print("Undo: Students added back.")






