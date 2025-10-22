class Student:
    def __init__(self, student_id: int, name: str, group: int):
        if group <= 0:
            raise ValueError("Group number must be a positive integer.")
        self.student_id = student_id
        self.name = name
        self.group = group

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Group: {self.group}"

