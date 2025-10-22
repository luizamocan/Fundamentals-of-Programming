from src.domain import *
from datetime import  date

from src.domain.exceptions import *
from src.services.undo_service import FunctionCall, Operation
from src.services.undo_service import *


class Services:
    def __init__(self, repository,undo_service):
        self.repository = repository
        self.undo_service = undo_service


    def add_book(self, book):
        for existing_book in self.repository.get_all_books():
            if existing_book.book_id == book.book_id:
                raise DuplicateBookError(book.book_id)

        self.repository.add_book(book)

        function_undo=FunctionCall(self.repository.remove_book, book.book_id)
        function_redo=FunctionCall(self.repository.add_book, book)
        self.undo_service.recordUndo(Operation(function_undo, function_redo))

    def remove_book_and_rentals(self, book_id):
        book = self.repository.find_book_by_id(book_id)
        if not book:
            raise BookNotFoundError(book_id)
        rentals = self.repository.find_rentals_by_book_id(book_id)

        previous_book_data = (book_id, book.title, book.author)
        previous_rentals_data = [(rental.rental_id, rental.book_id, rental.client_id, rental.rental_date) for rental in
                                 rentals]


        self.repository.remove_book(book_id)
        for rental in rentals:
            self.repository.remove_rental(rental.rental_id)


        function_undo_book = FunctionCall(self.repository.add_book, *previous_book_data)
        function_redo_book = FunctionCall(self.repository.remove_book, book_id)


        function_undo_rentals = [FunctionCall(self.repository.add_rental, *rental_data) for rental_data in
                                 previous_rentals_data]
        function_redo_rentals = [FunctionCall(self.repository.remove_rental, rental.rental_id) for rental in rentals]


        undo_operations = [function_undo_book] + function_undo_rentals
        redo_operations = [function_redo_book] + function_redo_rentals


        self.undo_service.recordUndo(CascadeOperation(*undo_operations))
        self.undo_service.recordUndo(CascadeOperation(*redo_operations))

    def update_book(self, book_id, new_title, new_author):
        book=self.repository.find_book_by_id(book_id)
        if not book:
            raise BookNotFoundError(book_id)

        previous_title=book.title
        previous_author=book.author
        self.repository.update_book(book_id, new_title, new_author)

        function_undo=FunctionCall(self.repository.update_book, book_id,previous_title, previous_author)
        function_redo=FunctionCall(self.repository.update_book, book_id, new_title, new_author)
        self.undo_service.recordUndo(Operation(function_undo, function_redo))

    def list_books(self):
        # no need for undo/redo
        return self.repository.get_all_books()

    def add_client(self, client):
        for existing_client in self.repository.get_all_clients():
            if existing_client.client_id == client.client_id:
                raise DuplicateClientError(client.client_id)

        self.repository.add_client(client)
        function_undo = FunctionCall(self.repository.remove_client, client.client_id)
        function_redo = FunctionCall(self.repository.add_client, client)
        self.undo_service.recordUndo(Operation(function_undo, function_redo))

    def remove_client_and_rentals(self, client_id):
        client = self.repository.find_client_by_id(client_id)
        if not client:
            raise ClientNotFoundError(client_id)

        rentals=self.repository.find_rentals_by_client_id(client_id)
        previous_client_data=(client.client_id, client.name)
        previous_rentals_data=[(rental.rental_id,rental.book_id, rental.client_id, rental.rented_date) for rental in rentals]
        self.repository.remove_client(client_id)
        for rental in rentals:
            self.repository.remove_rental(rental.rental_id)

        function_undo_client = FunctionCall(self.repository.add_client, *previous_client_data)
        function_redo_client = FunctionCall(self.repository.remove_client, client_id)

        #  undo/redo for rental removals
        function_undo_rentals = [FunctionCall(self.repository.add_rental, *rental_data) for rental_data in
                                 previous_rentals_data]
        function_redo_rentals = [FunctionCall(self.repository.remove_rental, rental.rental_id) for rental in rentals]

        undo_operations = [function_undo_client] + function_undo_rentals
        redo_operations = [function_redo_client] + function_redo_rentals

        self.undo_service.recordUndo(CascadeOperation(*undo_operations))
        self.undo_service.recordUndo(CascadeOperation(*redo_operations))

    def update_client(self, client_id, new_name):
        client=self.repository.find_client_by_id(client_id)
        if not client:
            raise ClientNotFoundError(client_id)

        previous_name=client.name
        self.repository.update_client(client_id, new_name)

        function_undo=FunctionCall(self.repository.update_client, client_id, previous_name)
        function_redo=FunctionCall(self.repository.update_client, client_id, new_name)
        self.undo_service.recordUndo(Operation(function_undo, function_redo))

    def list_clients(self):
        # no need for undo/redo
        return self.repository.get_all_clients()

    def rent_book(self, rental_id, book_id, client_id):
        rental_active=self.repository.find_active_rental_by_book(book_id)
        if rental_active:
            raise BookAlreadyRentedError(book_id)
        rental=Rental(rental_id, book_id, client_id, date.today())

        self.repository.add_rental(rental)
        function_undo=FunctionCall(self.repository.remove_rental, rental.rental_id)
        function_redo=FunctionCall(self.repository.add_rental, rental)
        self.undo_service.recordUndo(Operation(function_undo, function_redo))


    def return_book(self, rental_id):
        rental = self.repository.find_rental_by_id(rental_id)
        if rental:
            if rental.is_active():
                return_date = date.today()
                self.repository.return_rental(rental_id, return_date)
                function_undo = FunctionCall(self.repository.revert_rental_return, rental_id,
                                            None)
                function_redo = FunctionCall(self.repository.return_rental, rental_id,
                                            return_date)

                self.undo_service.recordUndo(Operation(function_undo, function_redo))
            else:
                raise RentalError(f"Rental with ID {rental_id} has already been returned.")
        else:
            raise RentalError(f"Rental with ID {rental_id} not found.")


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


    def most_rented_books(self, books, rentals):
        book_rent_count={}
        for rental in rentals:
            if rental.book_id not in book_rent_count:
                book_rent_count[rental.book_id]=0
            book_rent_count[rental.book_id] += 1

        for i in range(len(books)):
            for j in range(i + 1, len(books)):
                book_i_count = book_rent_count.get(books[i].book_id, 0)
                book_j_count = book_rent_count.get(books[j].book_id, 0)

                if book_i_count < book_j_count:
                    books[i], books[j] = books[j], books[i]
        return books

    def most_active_clients(self, clients,rentals):
        client_rental_days={}
        for rental in rentals:
            if rental.client_id not in client_rental_days:
                client_rental_days[rental.client_id]=0
            if self.repository.find_client_by_id(rental.client_id):
                rental_days=(datetime.date.today()-rental.rented_date).days
            else:
                rental_days=(rental.returned_date-rental.rented_date).days
            client_rental_days[rental.client_id]+= rental_days

        for i in range(len(clients)):
            for j in range(i + 1, len(clients)):
                client_i_days = client_rental_days.get(clients[i].client_id, 0)
                client_j_days = client_rental_days.get(clients[j].client_id, 0)

                if client_i_days < client_j_days:
                    clients[i], clients[j] = clients[j], clients[i]
        return clients

    def most_rented_authors(self, books, rentals):
        author_rent_count={}
        for rental in rentals:
            book = next(book for book in books if book.book_id == rental.book_id)
            if book.author not in author_rent_count:
                author_rent_count[book.author] = 0
            author_rent_count[book.author] += 1
        authors = list(set(book.author for book in books))


        for i in range(len(authors)):
            for j in range(i + 1, len(authors)):

                author_i_count = author_rent_count.get(authors[i], 0)
                author_j_count = author_rent_count.get(authors[j], 0)


                if author_i_count < author_j_count:
                    authors[i], authors[j] = authors[j], authors[i]

        return authors
    def get_all_books(self):
        return self.repository.get_all_books()
    def get_all_clients(self):
        return self.repository.get_all_clients()
    def get_all_rentals(self):
        return self.repository.get_all_rentals()