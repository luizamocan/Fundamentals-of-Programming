import datetime
class Book:
    """
Represents a book with details like ID, title, and author.

Attributes:
book_id (int): Unique identifier for the book.
title (str): Title of the book.
author (str): Author of the book.
    """
    def __init__(self, book_id:int , title: str, author:str):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__ (self):
        return f"book_id: {self.book_id}, title: {self.title}, author: {self.author}"

class Client:
    """
Represents a client with details like ID and name.

Attributes:
client_id (int): Unique identifier for the client.
name (str): Name of the client.
    """
    def __init__(self, client_id:int , name:str):
        self.client_id = client_id
        self.name = name

    def __str__ (self):
        return f"client_id: {self.client_id}, name: {self.name}"



class Rental:
    def __init__(self, rental_id:int , book_id:int , client_id:int , rented_date:datetime.date, returned_date:datetime.date=None):
        self.rental_id = rental_id
        self.book_id = book_id
        self.client_id = client_id
        self.rented_date = rented_date
        self.returned_date = returned_date

    def is_active(self):
        return self.returned_date is None

    def __str__(self):
        returned_date_str = self.returned_date if self.returned_date else "Not returned"
        return f"Rental ID: {self.rental_id}, Book ID: {self.book_id}, Client ID: {self.client_id}, Rented Date: {self.rented_date}, Returned Date: {returned_date_str}"