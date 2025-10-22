from src.domain import *
from src.services import *
from src.repository import *
from src.repository.data_generator import generate_data


def display_menu():
    print("1. Manage clients and books")
    print("2. Rent or return a book")
    print("3. Search for books or clients using one of their fields")
    print("4. See the statistics")
    print("0. Exit")


class UI:
    def __init__(self,services):
        self.services = services

    def undo_last_operation(self):
        try:
            self.services.undo_service.undo()
        except UndoError as error:
            print(error)

    def redo_last_operation(self):
        try:
            self.services.undo_service.redo()
        except UndoError as error:
            print(error)

    def manage_clients_and_books(self):
       while True:
            print("1. Add a client")
            print("2. Add a book")
            print("3. Remove a client")
            print("4. Remove a book")
            print("5. Update a client")
            print("6. Update a book")
            print("7. List the clients")
            print("8. List the books")
            print("9. Undo the last operation")
            print("10. Redo the last operation")
            print("0. Back to main menu")
            choice=input("Enter your choice: ")
            if choice=="1":
                try:
                    client_id=int(input("Enter client id: "))
                    name=input("Enter client name: ")
                    client=Client(client_id,name)
                    self.services.add_client(client)
                    print("Client added successfully")
                except DuplicateClientError as e:
                    print(f"Error: {e}")

            elif choice=="2":
                try:
                    book_id=int(input("Enter book id: "))
                    title=input("Enter book title: ")
                    author=input("Enter book author: ")
                    book=Book(book_id,title,author)
                    self.services.add_book(book)
                    print("Book added successfully")

                except DuplicateBookError as e:
                    print(f"Error: {e}")

            elif choice=="3":
                try:
                    client_id=int(input("Enter client id you want to remove: "))
                    self.services.remove_client_and_rentals(client_id)
                    print("Client removed successfully")
                except ClientNotFoundError as e:
                    print(f"Error: {e}")

            elif choice=="4":
                try:
                    book_id=int(input("Enter book id you want to remove: "))
                    self.services.remove_book_and_rentals(book_id)
                    print("Book removed successfully")
                except BookNotFoundError as e:
                    print(f"Error: {e}")

            elif choice=="5":
                try:
                    client_id=int(input("Enter client id you want to update: "))
                    new_name=input("Enter new name: ")
                    self.services.update_client(client_id,new_name)
                    print("Client updated successfully")
                except ClientNotFoundError as e:
                    print(f"Error: {e}")

            elif choice=="6":
                try:
                    book_id=int(input("Enter book id you want to update: "))
                    new_title=input("Enter new title: ")
                    new_author=input("Enter new author: ")
                    self.services.update_book(book_id,new_title,new_author)
                    print("Book updated successfully")
                except BookNotFoundError as e:
                    print(f"Error: {e}")

            elif choice=="7":
                print("Clients: ")
                for client in self.services.list_clients():
                    print(client)

            elif choice=="8":
                print("Books: ")
                for book in self.services.list_books():
                    print(book)

            elif choice=="9":
                self.undo_last_operation()

            elif choice=="10":
                self.redo_last_operation()


            elif choice=="0":
                break

            else:
                print("Invalid choice. Please try again.")

    def rent_or_return_book(self):
        while True:
            print("1. Rent a book")
            print("2. Return a book")
            print("3. List all rentals")
            print("4. Undo last operation")
            print("5. Redo last operation")
            print("0. Back to main menu")
            choice=input("Enter your choice: ")
            if choice=="1":
                try:
                    rental_id=int(input("Enter rental id: "))
                    book_id=int(input("Enter book id: "))
                    client_id=int(input("Enter client id: "))
                    self.services.rent_book(rental_id,book_id,client_id)
                    print("Book rented successfully")
                except BookNotFoundError as e:
                    print(f"Error: {e}")

            elif choice=="2":
                try:
                    rental_id=int(input("Enter rental id to return: "))
                    self.services.return_book(rental_id)
                    print("Book returned")
                except RentalError as e:
                    print(f"Error: {e}")

            elif choice=="3":
                print("Rentals: ")
                for rental in self.services.get_all_rentals():
                    print(rental)

            elif choice=="4":
                self.undo_last_operation()

            elif choice=="5":
                self.redo_last_operation()

            elif choice=="0":
                break

            else :
                print("Invalid choice. Please try again.")

    def search_books_and_clients(self):
        while True:
            print("1. Search for books")
            print("2. Search for clients")
            print("0. Back to main menu")
            choice=input("Enter your choice: ")
            if choice=="1":
                field=input("Search books by id/title/author: ")
                query=input("Enter search query: ")
                try:
                    results=self.services.search_books(field,query)
                    if results:
                        print("Books found")
                        for book in results:
                            print(book)
                    else:
                        print("Books not found")
                except InvalidSearchError as e:
                    print(f"Error: {e}")

            elif choice=="2":
                field=input("Search clients by id/name: ").lower()
                query=input("Enter search query: ")
                try:
                    results=self.services.search_clients(field,query)
                    if results:
                        print("Clients found")
                        for client in results:
                            print(client)
                    else:
                        print("Clients not found")
                except InvalidSearchError as e:
                    print(f"Error: {e}")

            elif choice=="0":
                break

            else:
                print("Invalid choice. Please try again.")

    def statistics(self):
        while True:
            print("1. Most rented books")
            print("2. Most active clients")
            print("3. Most rented author")
            print("0. Back to main menu")
            choice = input("Enter your choice: ")

            if choice == "0":
                break
            elif choice == "1":
                books = self.services.get_all_books()
                rentals = self.services.get_all_rentals()
                most_rented_books = self.services.most_rented_books(books, rentals)
                print("Most rented books:")
                for book in most_rented_books:
                    rent_count = sum(
                        1 for rental in rentals if rental.book_id == book.book_id)
                    print(f" Book Id: {book.book_id}, Book Title: {book.title} (Rented {rent_count} times)")

            elif choice == "2":
                clients = self.services.get_all_clients()
                rentals = self.services.get_all_rentals()
                most_active_clients = self.services.most_active_clients(clients, rentals)
                print("Most active clients:")
                for client in most_active_clients:
                    rental_days = sum(
                        (datetime.date.today() - rental.rented_date).days if rental.returned_date is None else (
                                    rental.returned_date - rental.rented_date).days
                        for rental in rentals if rental.client_id == client.client_id)
                    print(f"Client Id: {client.client_id}, Client name: {client.name} (Rented for {rental_days} days)")
            elif choice == "3":
                books = self.services.get_all_books()
                rentals = self.services.get_all_rentals()
                most_rented_authors = self.services.most_rented_authors(books, rentals)
                print("Most rented authors:")
                for author in most_rented_authors:
                    rent_count = sum(1 for rental in rentals if next(book for book in books if
                                                                     book.book_id == rental.book_id).author == author)
                    print(
                        f"Author: {author}, Author ID: {next(book for book in books if book.author == author).book_id} (Rented {rent_count} times)")
            else:
                print("Invalid choice, please try again.")

    def menu(self):
        while True:
            display_menu()
            choice=input("Enter your choice: ")

            if choice=="1":
                self.manage_clients_and_books()

            elif choice=="2":
                self.rent_or_return_book()

            elif choice=="3":
                self.search_books_and_clients()

            elif choice=="4":
                self.statistics()

            elif choice=="0":
                break

            else:
                print("Invalid choice. Please try again.")

def main():
    books, clients, rentals = generate_data()
    print("Choose repository type: ")
    print("1. Memory Repository")
    print("2. Text File Repository")
    print("3. Binary File Repository")
    choice=input("Enter your choice: ")
    if choice=="1":
        repo=MemoryRepository(books,clients,rentals)
    elif choice=="2":
        repo=TextFileRepository("../../book.txt", "../../client.txt", "../../rental.txt")
    elif choice=="3":
        repo=BinaryFileRepository("books.bin", "clients.bin", "rentals.bin")
    else:
        print("Invalid choice. Defaulting to Memory Repository.")
        repo=MemoryRepository()

    undo_service=UndoService()
    services=Services(repo,undo_service)
    ui=UI(services)
    ui.menu()


if __name__ == "__main__":
    main()


