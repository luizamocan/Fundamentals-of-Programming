from faker import Faker
import random
from datetime import timedelta
from src.domain import Book, Client, Rental

def generate_data():
    fake = Faker()
    books=[]
    clients=[]
    rentals=[]

    for i in range(1,21):
        book=Book(
            book_id=i,
            title=fake.sentence(nb_words=3),
            author=fake.name()
        )
        books.append(book)
    for i in range(1,21):
        client=Client(
            client_id=i,
            name=fake.name(),
        )
        clients.append(client)

    for i in range(1,21):
        book=random.choice(books)
        client=random.choice(clients)
        rental=Rental(
            rental_id=i,
            book_id=book.book_id,
            client_id=client.client_id,
            rented_date=fake.date_this_year(),
            returned_date=None
        )
        rentals.append(rental)

    returned_rentals = random.sample(rentals, 10)
    for rental in returned_rentals:
        rented_date = rental.rented_date
        return_days = random.randint(1, 30)
        rental.returned_date = rented_date + timedelta(days=return_days)

    return books,clients,rentals