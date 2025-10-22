class LibraryError(Exception):
    pass

class BookNotFoundError(LibraryError):
    def __init__(self, book_id):
        super().__init__(f"Book with ID {book_id} not found.")

class ClientNotFoundError(LibraryError):
    def __init__(self, client_id):
        super().__init__(f"Client with ID {client_id} not found.")

class DuplicateBookError(LibraryError):
    def __init__(self, book_id):
        super().__init__(f"Book with ID {book_id} already exists.")

class DuplicateClientError(LibraryError):
    def __init__(self, client_id):
        super().__init__(f"Client with ID {client_id} already exists.")

class RentalError(LibraryError):
    pass

class BookAlreadyRentedError(RentalError):
    def __init__(self, book_id):
        super().__init__(f"Book with ID {book_id} is already rented.")

class InvalidSearchError(LibraryError):
    def __init__(self, field):
        super().__init__(f"Invalid search field: {field}.")

class UndoError(Exception):
    pass