
from repository import TextFileRepository
from services import Services

class UI:
    def __init__(self,services):
        self.services = services

    def display_menu(self):
        print("1. Display the drivers sorted in increasing order of their name")
        print("2. Display the addresses sorted in increasing order of their name")
        print("3. Print all the drivers sorted by the distance to a given address id")
        print("4. Print the driver closest to each address")
        print("0. Exit")

    def menu(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "0":
                break

            if choice == "1":
                self.services.sort_drivers_by_name()
                drivers = self.services.get_all_drivers()
                for driver in drivers:
                    print(driver)

            if choice == "2":
                self.services.sort_addresses_by_name()
                addresses = self.services.get_all_addresses()
                for address in addresses:
                    print(address)

            if choice == "3":
                address_id = input("Enter the address ID: ")
                try:
                    drivers_sorted = self.services.get_drivers_sorted_by_distance(address_id)
                    for driver, distance in drivers_sorted:
                        print(f"{driver} - Distance: {distance}")
                except ValueError as e:
                    print(e)

            if choice == "4":
                closest_pairs = self.services.get_closest_drivers_for_addresses_sorted_by_distance()
                for address, driver, distance in closest_pairs:
                    print(
                        f"Address: {address}, Closest Driver: {driver}, Distance: {distance}"
                    )


def main():
    repo=TextFileRepository("drivers.txt", "addresses.txt")
    services=Services(repo)
    ui=UI(services)
    ui.menu()


if __name__ == "__main__":
    main()