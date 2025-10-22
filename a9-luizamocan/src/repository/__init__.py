import pickle
from src.domain import *
from src.domain.exceptions import *


class MemoryRepository:
    """
A repository that stores books and clients in memory (in lists) and provides CRUD operations.

Attributes:
_books (List[Book]): A list to store book objects.
_clients (List[Client]): A list to store client objects.
_rentals (List[Rental]): A list to store rental objects (optional for current specifications)
    """
    def __init__(self, initial_books=None, initial_clients=None, initial_rentals=None):
        self._books=initial_books or []
        self._clients=initial_clients or []
        self._rentals=initial_rentals or []

    #books related functions
    def find_book_by_id(self, book_id):
        return next((book for book in self._books if book.book_id == book_id), None)

    def add_book(self, book):
        """
Description: Adds a book to the repository.
Parameters: book (Book): The book to add.
Returns: None
Raises: DuplicateBookError if the book already exists (same book_id)
        """
        self._books.append(book)

    def remove_book(self, book_id):
        """
Description: Removes a book from the repository by its ID.
Parameters: book_id (int): The unique ID of the book to remove.
Returns: None
Raises: BookNotFoundError if the book with the given ID does not exist.
        """
        book=self.find_book_by_id(book_id)
        if book:
            self._books.remove(book)
        else:
            raise BookNotFoundError

    def update_book(self, book_id, new_title, new_author):
        """
Description: Updates the title and author of an existing book.
Parameters:
book_id (int): The unique ID of the book to update.
new_title (str): The new title of the book.
new_author (str): The new author of the book.
Returns: None
Raises: BookNotFoundError if the book with the given ID does not exist.
        """
        book = self.find_book_by_id(book_id)
        if not book:
            raise BookNotFoundError
        book.title = new_title
        book.author = new_author

    def get_all_books(self):
        """
Description: Retrieves all books in the repository.
Returns: List[Book]: List of all book objects.
        """
        return self._books

    #clients related functions
    def find_client_by_id(self, client_id):
        return next((client for client in self._clients if client.client_id == client_id), None)

    def add_client(self, client):
        """
Description: Adds a client to the repository.
Parameters: client (Client): The client to add.
Returns: None
Raises: DuplicateClientError if the client already exists (same client_id).
        """
        self._clients.append(client)

    def remove_client(self, client_id):
        """
Description: Removes a client from the repository by its ID.
Parameters: client_id (int): The unique ID of the client to remove.
Returns: None
Raises: ClientNotFoundError if the client with the given ID does not exist.
        """
        client=self.find_client_by_id(client_id)
        if client:
            self._clients.remove(client)
        else:
            raise ClientNotFoundError(client_id)

    def update_client(self, client_id, new_name):
        """
Description: Updates the name of an existing client.
Parameters:
client_id (int): The unique ID of the client to update.
new_name (str): The new name of the client.
Returns: None
Raises: ClientNotFoundError if the client with the given ID does not exist.

        """
        client=self.find_client_by_id(client_id)
        if not client:
            raise ClientNotFoundError
        client.name = new_name


    def get_all_clients(self):
        """
Description: Retrieves all clients in the repository.
Returns: List[Client]: List of all client objects
        """
        return self._clients

    #rental related functions
    def find_rental_by_id(self, rental_id):
        return next((rental for rental in self._rentals if rental.rental_id == rental_id ), None)

    def find_active_rental_by_book(self, book_id):
        return next((rental for rental in self._rentals if rental.book_id == book_id and rental.is_active()), None)

    def find_rentals_by_client_id(self, client_id):
        return [rental for rental in self._rentals if rental.client_id == client_id]

    def find_rentals_by_book_id(self, book_id):
        return [rental for rental in self._rentals if rental.book_id == book_id]

    def add_rental(self, rental):
        self._rentals.append(rental)

    def remove_rental(self, rental_id):
        rental = self.find_rental_by_id(rental_id)
        if rental:
            self._rentals.remove(rental)
        else:
            raise RentalError(f"Rental with ID {rental_id} not found.")

    def return_rental(self, rental_id, returned_date):
        rental = self.find_rental_by_id(rental_id)
        if rental:
            if rental.is_active():
                rental.returned_date = returned_date
            else:
                raise RentalError(f"Rental with ID {rental_id} has already been returned.")
        else:
            raise RentalError(f"Rental with ID {rental_id} not found.")

    def revert_rental_return(self, rental_id, previous_date):
        rental = self.find_rental_by_id(rental_id)
        if rental:
            if rental.returned_date is not None:
                rental.returned_date = previous_date
            else:
                raise RentalError(f"Rental with ID {rental_id} is already active.")
        else:
            raise RentalError(f"Rental with ID {rental_id} not found.")

    def get_all_rentals(self):
         return self._rentals

    def search_books_by_field(self,field, query):
        query=query.lower()
        if field== "id":
            return [book for book in self._books if query == str(book.book_id)]
        elif field== "title":
            return [book for book in self._books if query in book.title.lower()]
        elif field== "author":
            return [book for book in self._books if query in book.author.lower()]
        else:
            raise InvalidSearchError(field)

    def search_clients_by_field(self,field, query):
        query=query.lower()
        if field== "id":
            return [client for client in self._clients if query== str(client.client_id)]
        elif field== "name":
            return [client for client in self._clients if query in client.name.lower()]
        else:
            raise InvalidSearchError(field)




class TextFileRepository(MemoryRepository):
    def __init__(self, file_book, file_client, file_rental):
        super().__init__()
        self.file_book = file_book
        self.file_client = file_client
        self.file_rental = file_rental
        self._books = []
        self._clients = []
        self._rentals = []
        self._load()




    def _load(self):
            with open(self.file_book, "r") as file1:
                for line in file1:
                    book_id, title, author = line.strip().split(",")
                    self.add_book(Book(int(book_id), title, author))

            with open(self.file_client, "r") as file2:
                for line2 in file2:
                    client_id, name = line2.strip().split(",")
                    self.add_client(Client(int(client_id), name))


            with open(self.file_rental, "r") as file3:
                for line3 in file3:
                    rental_id, book_id, client_id, rented_date, returned_date = line3.strip().split(",")
                    rental = Rental(
                        int(rental_id), int(book_id), int(client_id),
                        datetime.date.fromisoformat(rented_date),
                        datetime.date.fromisoformat(returned_date) if returned_date != "None" else None
                        )
                    self.add_rental(rental)




    def _save(self):
        # Save books
        with open(self.file_book, "w") as file1:
            for book in self._books:
                file1.write(f"{book.book_id},{book.title},{book.author}\n")

        # Save clients
        with open(self.file_client, "w") as file2:
            for client in self._clients:
                file2.write(f"{client.client_id},{client.name}\n")

        # Save rentals
        with open(self.file_rental, "w") as file3:
            for rental in self._rentals:
                returned_date = rental.returned_date.isoformat() if rental.returned_date else "None"
                file3.write(
                    f"{rental.rental_id},{rental.book_id},{rental.client_id},{rental.rented_date.isoformat()},{returned_date}\n")

    def add_book(self, book):
        super().add_book(book)
        self._save()

    def add_client(self, client):
        super().add_client(client)
        self._save()

    def remove_book(self, book_id):
        super().remove_book(book_id)
        self._save()

    def remove_client(self, client_id):
        super().remove_client(client_id)
        self._save()

    def update_book(self,book_id, new_title, new_author):
        super().update_book(book_id, new_title, new_author)
        self._save()

    def update_client(self, client_id, new_name):
        super().update_client(client_id, new_name)
        self._save()


    def add_rental(self, rental):
        super().add_rental(rental)
        self._save()

    def return_rental(self, rental_id, returned_date):
        super().return_rental(rental_id, returned_date)
        self._save()

    def get_all_rentals(self):
        return super().get_all_rentals()


class BinaryFileRepository(MemoryRepository):
    def __init__(self, file_book, file_client, file_rental):
        super().__init__()
        self.file_book=file_book
        self.file_client=file_client
        self.file_rental=file_rental
        self._load()

    def _load(self):
        try:
            with open(self.file_book, "rb") as file1:
                self._books=pickle.load(file1)
            with open(self.file_client, "rb") as file2:
                self._clients=pickle.load(file2)
            with open(self.file_rental, "rb") as file3:
                self._rentals=pickle.load(file3)
        except FileNotFoundError:
            self._books=[]
            self._clients=[]
            self._rentals=[]
        except EOFError:
            self._books=[]
            self._clients=[]
            self._rentals=[]

    def _save(self):
        with open(self.file_book, "wb") as file:
            pickle.dump(self._books, file)
        with open(self.file_client, "wb") as file:
            pickle.dump(self._clients, file)
        with open(self.file_rental, "wb") as file:
            pickle.dump(self._rentals, file)

    def add_book(self, book):
        super().add_book(book)
        self._save()

    def remove_book(self, book_id):
        super().remove_book(book_id)
        self._save()

    def update_book(self, book_id, new_title, new_author):
        super().update_book(book_id, new_title, new_author)
        self._save()

    def add_client(self, client):
        super().add_client(client)
        self._save()

    def remove_client(self, client_id):
        super().remove_client(client_id)
        self._save()

    def update_client(self, client_id, new_name):
        super().update_client(client_id, new_name)
        self._save()

    def add_rental(self, rental):
        super().add_rental(rental)
        self._save()

    def return_rental(self, rental_id, returned_date):
        super().return_rental(rental_id, returned_date)
        self._save()

    def get_all_rentals(self):
        return super().get_all_rentals()

