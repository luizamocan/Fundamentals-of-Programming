#
# Functions section
#
def create_flight(code:str, duration:int, departure_city:str, destination_city:str)->list:
    return [code, duration, departure_city, destination_city]

def get_code(flight):
    return flight[0]

def get_duration(flight):
    return flight[1]

def get_departure_city(flight):
    return flight[2]

def get_destination_city(flight):
    return flight[3]

def to_string(flight):
    code=get_code(flight)
    duration=get_duration(flight)
    departure_city=get_departure_city(flight)
    destination_city=get_destination_city(flight)
    return code, duration, departure_city, destination_city



def add_flight(flights:list, code:str,duration:int, departure_city:str, destination_city:str):
    if len(code)<3:
        raise ValueError("Code must be at least 3 characters")
    if len(departure_city)<3:
        raise ValueError("Departure city must be at least 3 characters")
    if len(destination_city)<3:
        raise ValueError("Destination city must be at least 3 characters")
    if duration<20:
        raise ValueError("The flight must be at least 20 minutes")

    flight=create_flight(code,duration,departure_city,destination_city)
    flights.append(flight)
    return flights

def delete_flight(flights:list, code_delete:str):
    """
    The function removes the flight with the given code from the flight list
    :param flights: the list of flights
    :param code_delete: the code of the flight to be deleted
    :return: the updated flight list
    """
    for i in range(len(flights)-1, -1, -1):
        code=get_code(flights[i])
        if code==code_delete:
            flights.pop(i)

    return flights

def test_delete():
    flights=[]
    add_flight(flights, "0b3002", 45, "Cluj-Napoca", "London")
    add_flight(flights, "1B2986", 60, "Cluj-Napoca", "Berlin")
    add_flight(flights, "35FG750", 30, "Bucharest", "Budapest")
    assert len(flights)==3

    delete_flight(flights, "35FG750")
    assert len(flights)==2
    assert ["35FG750", 30, "Bucharest", "Budapest"] not  in flights


def sort_increasing_destination(flights:list):
    for i in range(len(flights)-1):
        for j in range(i+1,len(flights)):
            destination1=get_destination_city(flights[i])
            destination2=get_destination_city(flights[j])
            if destination1>destination2:
                flights[i],flights[j]=flights[j],flights[i]

    return flights

def print_flights(flights):
    for flight in flights:
        code=get_code(flight)
        duration=get_duration(flight)
        departure_city=get_departure_city(flight)
        destination_city=get_destination_city(flight)
        print(f"code:{code}, duration: {duration}, departure_city: {departure_city}, destination_city: {destination_city}")

def print_departure_city(flights:list, city:str):
    for flight in flights:
        code = get_code(flight)
        duration = get_duration(flight)
        departure_city = get_departure_city(flight)
        destination_city = get_destination_city(flight)
        if departure_city==city:
            print(f"code:{code}, duration: {duration}, departure_city: {departure_city}, destination_city: {destination_city}")



def modify_duration_flights(flights:list, city_delayed:str, delay:int):
    if delay<10 or delay>60:
        raise ValueError("Delay must be between 10 and 60 minutes")
    for i in range(len(flights)):
        departure_city=get_departure_city(flights[i])
        if departure_city==city_delayed:
            flights[i][1] = flights[i][1] + delay

    return flights

#
# User interface section
#
def print_menu():
    print("1. Add a flight")
    print("2. Delete a given flight")
    print("3. Show all flights with a given departure city")
    print("4. Modify the duration from a a given departure city due to delay")
    print("5. Print all the flights")
    print("0. Exit")

def menu():
    test_delete()
    flights=[]
    add_flight(flights, "0b3002", 45, "Cluj-Napoca","London" )
    add_flight(flights, "1B2986", 60, "Cluj-Napoca", "Berlin")
    add_flight(flights, "35FG750", 30, "Bucharest", "Sibiu")
    while True:
        print_menu()
        option=int(input("Enter your option: "))
        if option==0:
            break
        if option==1:
            try:
                code=input("Enter flight code: ")
                duration=int(input("Enter flight duration: "))
                departure_city=input("Enter departure city: ")
                destination_city=input("Enter destination city: ")
                add_flight(flights,code,duration,departure_city,destination_city)
                print("Flight added successfully")
            except ValueError as ve:
                print(ve)

        if option==2:
            code_delete=input("Enter flight code to delete: ")
            flights=delete_flight(flights,code_delete)
            print("Flight deleted successfully")

        if option==3:
            dep_city=input("Enter departure city: ")
            sort_increasing_destination(flights)
            print_departure_city(flights,dep_city)

        if option==4:
            try:
                city_delayed=input("Enter the city where it is a delay: ")
                delay=int(input("Enter the delay: "))
                flights=modify_duration_flights(flights, city_delayed, delay)
            except ValueError as v:
                print(v)

        if option==5:
            print_flights(flights)



def main():

    menu()

main()


