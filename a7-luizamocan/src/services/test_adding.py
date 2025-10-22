def test_services():

    from src.domain import Student
    from src.repository import MemoryRepository
    from src.services import Services

    repo = MemoryRepository()
    services = Services(repo)

    student1 = Student(11, "Ana", 911)
    services.add_student(student1)
    assert len(repo.get_all()) == 1

    student2 = Student(12, "Luiza", 915)
    services.add_student(student2)
    assert len(repo.get_all()) == 2