import unittest
from unittest.mock import MagicMock
from src.domain import Book, Client
from src.services import Services
from src.repository import MemoryRepository
from src.domain.exceptions import *


class TestServices(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.services = Services(self.mock_repo)

    def test_add_book_success(self):
        book = Book(1, "Test Book", "Test Author")
        self.mock_repo.find_book_by_id.return_value = None

        self.services.add_book(book)
        self.mock_repo.add_book.assert_called_once_with(book)

    def test_remove_book_success(self):
        book_id = 1
        self.mock_repo.find_book_by_id.return_value = Book(book_id, "Test Book", "Test Author")
        self.services.remove_book(book_id)
        self.mock_repo.remove_book.assert_called_once_with(book_id)

    def test_remove_book_not_found(self):
        book_id = 999
        self.mock_repo.find_book_by_id.return_value = None

        with self.assertRaises(BookNotFoundError):
            self.services.remove_book(book_id)

    def test_update_book_success(self):
        book_id = 1
        self.mock_repo.find_book_by_id.return_value = Book(book_id, "Old Title", "Old Author")
        new_title = "New Title"
        new_author = "New Author"
        self.services.update_book(book_id, new_title, new_author)
        self.mock_repo.update_book.assert_called_once_with(book_id, new_title, new_author)

    def test_list_books(self):
        books = [Book(i, f"Book {i}", f"Author {i}") for i in range(1, 4)]
        self.mock_repo.get_all_books.return_value = books
        result = self.services.list_books()
        self.assertEqual(result, books)
        self.mock_repo.get_all_books.assert_called_once()


class TestMemoryRepository(unittest.TestCase):
    def setUp(self):
        self.repo = MemoryRepository()

    def test_add_book(self):
        book = Book(1, "Test Book", "Test Author")
        self.repo.add_book(book)
        self.assertIn(book, self.repo.get_all_books())


    def test_remove_book(self):
        book = Book(1, "Test Book", "Test Author")
        self.repo.add_book(book)
        self.repo.remove_book(book.book_id)
        self.assertNotIn(book, self.repo.get_all_books())

    def test_add_client(self):
        client = Client(1, "Test Client")
        self.repo.add_client(client)
        self.assertIn(client, self.repo.get_all_clients())

    def test_remove_client(self):
        client = Client(1, "Test Client")
        self.repo.add_client(client)
        self.repo.remove_client(client.client_id)
        self.assertNotIn(client, self.repo.get_all_clients())

    def test_get_all_books(self):
        books = [Book(i, f"Book {i}", f"Author {i}") for i in range(1, 6)]
        for book in books:
            self.repo.add_book(book)
        self.assertEqual(self.repo.get_all_books(), books)

    def test_get_all_clients(self):
        clients = [Client(i, f"Client {i}") for i in range(1, 6)]
        for client in clients:
            self.repo.add_client(client)
        self.assertEqual(self.repo.get_all_clients(), clients)

    def test_find_book_by_id(self):
        book = Book(1, "Test Book", "Test Author")
        self.repo.add_book(book)
        self.assertEqual(self.repo.find_book_by_id(1), book)
        self.assertIsNone(self.repo.find_book_by_id(999))

    def test_find_client_by_id(self):
        client = Client(1, "Test Client")
        self.repo.add_client(client)
        self.assertEqual(self.repo.find_client_by_id(1), client)
        self.assertIsNone(self.repo.find_client_by_id(999))

    def test_search_books_by_title(self):
        book1 = Book(1, "The Great Adventure", "Author 1")
        book2 = Book(2, "The Lost Journey", "Author 2")
        self.repo.add_book(book1)
        self.repo.add_book(book2)
        result = self.repo.search_books_by_field("title", "adventure")
        self.assertIn(book1, result)
        self.assertNotIn(book2, result)

    def test_search_clients_by_name(self):
        client1 = Client(1, "Alice Johnson")
        client2 = Client(2, "Bob Smith")
        self.repo.add_client(client1)
        self.repo.add_client(client2)
        result = self.repo.search_clients_by_field("name", "alice")
        self.assertIn(client1, result)
        self.assertNotIn(client2, result)


if __name__ == "__main__":
    unittest.main()
