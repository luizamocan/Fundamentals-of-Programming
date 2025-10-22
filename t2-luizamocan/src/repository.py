from domain import Driver, Address

class MemoryRepository:
    def __init__(self):
        self._drivers=[]
        self._addresses=[]

    def get_all_drivers(self):
        return self._drivers

    def get_all_addresses(self):
        return self._addresses

    def sort_drivers_by_name(self):
        return sorted(self._drivers, key=lambda driver: driver.name, reverse=False)


    def sort_addresses_by_name(self):
        return sorted(self._addresses, key=lambda address: address.name, reverse=False)



    def get_drivers_sorted_by_distance(self, address_id):
        """
                Function that sorts the drivers by the Manhattan distance to a given address_id
                :param address_id: the id for the address we find the distance from
                :return: the drivers sorted
                """
        address = next(
            (addr for addr in self.get_all_addresses() if addr.id == address_id),
            None
        )

        drivers = self.get_all_drivers()
        drivers_with_distances = [
            (driver, abs(int(driver.x) - int(address.x)) + abs(int(driver.y) - int(address.y)))
            for driver in drivers
        ]
        drivers_sorted = sorted(drivers_with_distances, key=lambda item: item[1])
        return drivers_sorted

    def get_closest_drivers_for_addresses_sorted_by_distance(self):
        addresses = self.get_all_addresses()
        drivers = self.get_all_drivers()
        closest_driver_pairs = []

        for address in addresses:
            closest_driver = min(
                drivers,
                key=lambda driver: abs(int(driver.x) - int(address.x)) + abs(int(driver.y) - int(address.y))
            )
            distance = abs(int(closest_driver.x) - int(address.x)) + abs(int(closest_driver.y) - int(address.y))
            closest_driver_pairs.append((address, closest_driver, distance))


        closest_driver_pairs.sort(key=lambda item:item[2], reverse=True)
        return closest_driver_pairs


class TextFileRepository(MemoryRepository):
    def __init__(self, driver_file, address_file):
        super().__init__()
        self._driver_file = driver_file
        self._address_file = address_file
        self._load()


    def _load(self):
        try:
            with open(self._driver_file, 'r') as file:
                for line in file:
                    name,x,y=line.strip().split(",")
                    self._drivers.append(Driver(name,x,y))

            with open(self._address_file, 'r') as file:
                for line in file:
                    id,name,x,y=line.strip().split(",")
                    self._addresses.append(Address(id,name,x,y))


        except FileNotFoundError:
            pass


    def _save(self):
        with open(self._driver_file, 'w') as file:
            for driver in self._drivers:
                file.write(f"{driver.name},{driver.x},{driver.y}\n")

        with open(self._address_file, 'w') as file:
            for address in self._addresses:
                file.write(f"{address.id},{address.name},{address.x},{address.y}\n")



    def get_all_drivers(self):
        return super().get_all_drivers()

    def get_all_addresses(self):
        return super().get_all_addresses()

    def sort_drivers_by_name(self):
        sorted_drivers = super().sort_drivers_by_name()
        self._drivers = sorted_drivers
        self._save()
        return sorted_drivers

    def sort_addresses_by_name(self):
        sorted_addresses = super().sort_addresses_by_name()
        self._addresses = sorted_addresses
        self._save()
        return sorted_addresses


