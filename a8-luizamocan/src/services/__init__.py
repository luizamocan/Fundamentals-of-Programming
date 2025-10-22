from src.domain import *
from datetime import  date

from src.domain.exceptions import *


class Services:
    def __init__(self, repository):
        self.repository = repository


    def add_book(self, book):
        for existing_book in self.repository.get_all_books():
            if existing_book.book_id == book.book_id:
                raise DuplicateBookError(book.book_id)

        self.repository.add_book(book)

    def remove_book(self, book_id):
        book = self.repository.find_book_by_id(book_id)
        if book:
            self.repository.remove_book(book_id)
        else:
            raise BookNotFoundError(book_id)

    def update_book(self, book_id, new_title, new_author):
        self.repository.update_book(book_id, new_title, new_author)

    def list_books(self):
        return self.repository.get_all_books()

    def add_client(self, client):
        for existing_client in self.repository.get_all_clients():
            if existing_client.client_id == client.client_id:
                raise DuplicateClientError(client.client_id)

        self.repository.add_client(client)

    def remove_client(self, client_id):
        client = self.repository.find_client_by_id(client_id)
        if client:
            self.repository.remove_client(client_id)
        else:
            raise ClientNotFoundError(client_id)

    def update_client(self, client_id, new_name):
        self.repository.update_client(client_id, new_name)

    def list_clients(self):
        return self.repository.get_all_clients()

    def rent_book(self, rental_id, book_id, client_id):
        rental_active=self.repository.find_active_rental_by_book(book_id)
        if rental_active:
            raise BookAlreadyRentedError(book_id)
        rental=Rental(rental_id, book_id, client_id, date.today())
        self.repository.add_rental(rental)

    def return_book(self, rental_id):
        rental = self.repository.find_rental_by_id(rental_id)
        if rental:
            if rental.is_active():
                self.repository.return_rental(rental_id, date.today())
            else:
                raise RentalError(f"Rental with ID {rental_id} has already been returned.")
        else:
            raise RentalError(f"Rental with ID {rental_id} not found.")

    def get_all_rentals(self):
        return self.repository.get_all_rentals()

    def search_books(self, field, query):
        valid_fields=["id", "title", "author"]
        if field not in valid_fields:
            raise ValueError('Field must be one of {}'.format(valid_fields))
        return self.repository.search_books_by_field(field, query)

    def search_clients(self, field, query):
        valid_fields=["id", "name"]

        if field not in valid_fields:
            raise ValueError('Field must be one of {}'.format(valid_fields))
        return self.repository.search_clients_by_field(field, query)
