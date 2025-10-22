

class Services:
    def __init__(self,repository):
        self.repository = repository

    def get_all_drivers(self):
        return self.repository.get_all_drivers()

    def get_all_addresses(self):
        return self.repository.get_all_addresses()

    def sort_drivers_by_name(self):
        return self.repository.sort_drivers_by_name()

    def sort_addresses_by_name(self):
        return self.repository.sort_addresses_by_name()

    def get_drivers_sorted_by_distance(self, address_id):
        """
        Function that imports the main function from the repository layer
        :param address_id: the address id for which we find the Manhattan distances
        :return: the drivers sorted by that distance
        """
        return self.repository.get_drivers_sorted_by_distance(address_id)

    def get_closest_drivers_for_addresses_sorted_by_distance(self):
        return self.repository.get_closest_drivers_for_addresses_sorted_by_distance()