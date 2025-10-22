from src.domain import Student
from src.services import Services
from src.repository import MemoryRepository, TextFileRepository, BinaryFileRepository
from src.services import generate_students
from src.services.test_adding import test_services
import pickle
def view_binary_contents():
    try:
        with open('students.bin', 'rb') as file:
            students = pickle.load(file)
            if not students:
                print("No students found in the binary file.")
            else:
                for student in students:
                    print(student)
    except FileNotFoundError:
        print("No binary file found.")
    except EOFError:
        print("The binary file is empty.")


class UI:
    def __init__(self, services):
        self.services = services

    def display_menu(self):
        print("1. Add student")
        print("2. Display students")
        print("3. Remove students by group")
        print("4. Undo last operation")
        print("5. View binary contents")
        print("0. Exit")

    def menu(self):
        while True:
            self.display_menu()
            option = input("Choose an option: ")
            if option == "1":
                try:
                    student_id = int(input("Student ID: "))
                    name = input("Name: ")
                    group = int(input("Group: "))
                    student = Student(student_id, name, group)
                    self.services.add_student(student)
                    print("Student added successfully")
                except ValueError as e:
                    print(f"Error: {e}")

            elif option == "2":
                students = self.services.get_all_students()
                if not students:
                    print("No students found.")
                else:
                    for student in students:
                        print(student)

            elif option == "3":
                try:
                    group = int(input("Group to remove: "))
                    self.services.remove_students_by_group(group)
                    print("Students removed successfully")
                except ValueError:
                    print("Invalid input.")

            elif option == "4":
                try:
                    self.services.undo()
                except Exception as e:
                    print(f"Error: {e}")
            elif option == "5":
                view_binary_contents()

            elif option == "0":
                break

            else:
                print("Invalid option. Try again.")



def main():
    print("Choose repository type")
    print("1. Memory Repository")
    print("2. Text File Repository")
    print("3. Binary File Repository")
    choice = input("Choose repository type: ")
    if choice == "1":
        repo=MemoryRepository()
    elif choice == "2":
        repo = TextFileRepository("students.txt")
    elif choice == "3":
        repo = BinaryFileRepository("students.bin")

    else:
        print("Invalid choice. Defaulting to Memory Repository.")
        repo = MemoryRepository()

    repo.clear()  #clear the repository before starting

    students = generate_students(10)
    for student in students:
        repo.add(student)

    services = Services(repo)
    ui = UI(services)
    ui.menu()
    test_services()

if __name__ == "__main__":
    main()

