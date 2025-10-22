from src.domain import *
from src.services import *
from src.repository import *
from src.repository.data_generator import generate_data


def display_menu():
    print("1. Manage clients and books")
    print("2. Rent or return a book")
    print("3. Search for books or clients using one of their fields")
    print("0. Exit")


class UI:
    def __init__(self,services):
        self.services = services

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
                    self.services.remove_client(client_id)
                    print("Client removed successfully")
                except ClientNotFoundError as e:
                    print(f"Error: {e}")

            elif choice=="4":
                try:
                    book_id=int(input("Enter book id you want to remove: "))
                    self.services.remove_book(book_id)
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

            elif choice=="0":
                break

            else:
                print("Invalid choice. Please try again.")

    def rent_or_return_book(self):
        while True:
            print("1. Rent a book")
            print("2. Return a book")
            print("3. List all rentals")
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
        repo=TextFileRepository("books1.txt", "clients1.txt", "rentals1.txt")
    elif choice=="3":
        repo=BinaryFileRepository("books.bin", "clients.bin", "rentals.bin")
    else:
        print("Invalid choice. Defaulting to Memory Repository.")
        repo=MemoryRepository()

    services=Services(repo)
    ui=UI(services)
    ui.menu()


if __name__ == "__main__":
    main()

