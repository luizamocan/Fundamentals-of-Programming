#
# Write the implementation for A5 in this file
#
from  random import randint
# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def create_number_list(real_part: int, fractional_part: int)->list:
    if type(real_part) != int:
        raise TypeError("The real part must be an integer.")
    elif type(fractional_part) != int:
        raise TypeError("The fractional part must be an integer.")
    return [real_part, fractional_part]

def get_number_real_part_list(number):
    return number[0]

def get_number_fractional_part_list(number):
    return number[1]

def add_new_number_list(numbers:list):
    try:
        real_part = int(input("Enter the real part of the number: "))
    except ValueError:
        raise TypeError("The real part must be an integer.")

    try:
        fractional_part = int(input("Enter the fractional part of the number: "))
    except ValueError:
        raise TypeError("The fractional part must be an integer.")

    print(f"The new added number is: {real_part} + {fractional_part}i")
    number=create_number_list(real_part, fractional_part)
    numbers.append(number)

def to_str_list(number):
    real_part = get_number_real_part_list(number)
    fractional_part = get_number_fractional_part_list(number)
    return f"{real_part}+{fractional_part}i"


def generate_numbers_list(n: int):
    result=[]
    for i in range(n):
        real_part=randint(0,100)
        fractional_part= randint(0,100)
        number=create_number_list(real_part, fractional_part)
        result.append(number)

    return result


#Test functions for list representation
def test_create_number_list():
    assert create_number_list(3, 4) == [3, 4]
    assert create_number_list(24, 30) == [24, 30]
    assert create_number_list(1, 2) == [1, 2]

def test_get_number_real_part_list():
    assert get_number_real_part_list([3,4]) == 3
    assert get_number_real_part_list([24, 30]) == 24
    assert get_number_real_part_list([1, 2]) == 1

def test_get_number_fractional_part_list():
    assert get_number_fractional_part_list([3,4]) == 4
    assert get_number_fractional_part_list([24, 30]) == 30
    assert get_number_fractional_part_list([1, 2]) == 2

def test_to_str_list():
    assert to_str_list([3,4]) == "3+4i"
    assert to_str_list([24, 30]) == "24+30i"
    assert to_str_list([1, 2]) == "1+2i"

def test_generate_numbers_list():
    numbers = generate_numbers_list(5)
    assert len(numbers) == 5
    for num in numbers:
        assert isinstance(num, list) and len(num) == 2
        assert 0 <= num[0] <= 100 and 0 <= num[1] <= 100


# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def create_number_dict(real_part:int, fractional_part:int)->dict:
    if type(real_part) != int:
        raise TypeError("The real part must be an integer.")
    elif type(fractional_part) != int:
        raise TypeError("The fractional part must be an integer.")

    return {"real_part": real_part, "fractional_part": fractional_part}

def get_number_real_part_dict(number):
    return number["real_part"]

def get_number_fractional_part_dict(number):
    return number["fractional_part"]

def add_new_number_dict(numbers):
    try:
        real_part = int(input("Enter the real part of the number: "))
    except ValueError:
        raise TypeError("The real part must be an integer.")

    try:
        fractional_part = int(input("Enter the fractional part of the number: "))
    except ValueError:
        raise TypeError("The fractional part must be an integer.")

    print(f"The new added number is: {real_part} + {fractional_part}i")
    number=create_number_dict(real_part, fractional_part)
    numbers.append(number)

def to_str_dict(number):
    real_part = get_number_real_part_dict(number)
    fractional_part = get_number_fractional_part_dict(number)
    return f"{real_part}+{fractional_part}i"


def generate_numbers_dict(n: int):
    result=[]
    for i in range(n):
        real_part=randint(0,100)
        fractional_part= randint(0,100)
        number=create_number_dict(real_part, fractional_part)
        result.append(number)

    return result

#Test functions for dict representation
def test_create_number_dict():
    assert create_number_dict(3, 4) == {"real_part": 3, "fractional_part": 4}
    assert create_number_dict(24, 30) == {"real_part": 24, "fractional_part": 30}
    assert create_number_dict(1, 2) == {"real_part": 1, "fractional_part": 2}

def test_get_number_real_part_dict():
    assert get_number_real_part_dict({"real_part": 3, "fractional_part": 4}) == 3
    assert get_number_real_part_dict({"real_part": 24, "fractional_part": 30}) == 24
    assert get_number_real_part_dict({"real_part": 1, "fractional_part": 2}) == 1

def test_get_number_fractional_part_dict():
    assert get_number_fractional_part_dict({"real_part": 3, "fractional_part": 4}) == 4
    assert get_number_fractional_part_dict({"real_part": 24, "fractional_part": 30}) == 30
    assert get_number_fractional_part_dict({"real_part": 1, "fractional_part": 2}) == 2

def test_to_str_dict():
    assert to_str_dict({"real_part": 3, "fractional_part": 4}) == "3+4i"
    assert to_str_dict({"real_part": 24, "fractional_part": 30}) == "24+30i"
    assert to_str_dict({"real_part": 1, "fractional_part": 2}) == "1+2i"

def test_generate_numbers_dict():
    numbers = generate_numbers_dict(5)
    assert len(numbers) == 5
    for num in numbers:
        assert isinstance(num, dict)



# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
def longest_subarray(numbers):
    result=0
    len_max=0
    for i in range(len(numbers)):
        current_subarray=[]
        distinct_values=[]
        for j in range(i,len(numbers)):
            current_subarray.append(numbers[j])
            if numbers[j] not in distinct_values:
                distinct_values.append(numbers[j])

            if len(distinct_values)>3:
                break

            if len(current_subarray)>len_max:
                len_max=len(current_subarray)
                result=current_subarray.copy()

    return len_max, result

def initialise_dp(n: int):
    up=[]
    down=[]
    for i in range(n):
        up.append(1)
    for j in range(n):
        down.append(1)
    return up,down

def fill_dp(numbers,up,down):
    n = len(numbers)
    for i in range(n):
        for j in range(i):
            # real_i=get_number_real_part_list(numbers[i])
            # real_j = get_number_real_part_list(numbers[j])
            real_i=get_number_real_part_dict(numbers[i])
            real_j = get_number_real_part_dict(numbers[j])

            if real_i > real_j:
                up[i] = max(up[i], down[j] + 1)
            elif real_i < real_j:
                down[i] = max(down[j], up[i] + 1)



def get_max_length(up, down) -> int:
    return max(max(up), max(down))


# Function to reconstruct the longest alternating subsequence
def reconstruct_subsequence(numbers,up,down,max_length):
    subsequence = []
    current_length = max_length
    current_list = up if max(up) == max_length else down

    for i in range(len(numbers) - 1, -1, -1):
        # if (current_list == up and (i == 0 or get_number_real_part_list(numbers[i]) > get_number_real_part_list(numbers[i-1]))) or \
        #  (current_list == down and (i == 0 or get_number_real_part_list(numbers[i]) < get_number_real_part_list(numbers[i-1]))):
         if (current_list == up and (i == 0 or get_number_real_part_dict(numbers[i]) > get_number_real_part_dict(numbers[i-1]))) or \
               (current_list == down and (i == 0 or get_number_real_part_dict(numbers[i]) < get_number_real_part_dict(numbers[i-1]))):
            subsequence.insert(0, numbers[i])
            current_length -= 1
            if current_length == 0:
                break
            current_list = down if current_list == up else up

    return subsequence



def longest_alternating_subsequence(numbers):
    n = len(numbers)
    if n == 0:
        return 0, []

    up, down = initialise_dp(len(numbers))
    fill_dp(numbers,  up, down)
    max_length = get_max_length(up, down)
    subsequence = reconstruct_subsequence(numbers,  up, down, max_length)
    return max_length, subsequence


#Test functions for the subarray/subsequence properties
def test_longest_subarray():
    numbers1 = [1, 2, 2, 3, 3, 1, 1, 2]
    length1, subarray1 = longest_subarray(numbers1)
    assert length1 == 8
    assert subarray1 == [1,2,2,3,3,1,1,2]

    numbers2=[1,2,3,4,5,6]
    length2, subarray2 = longest_subarray(numbers2)
    assert length2 == 3
    assert subarray2 == [1, 2, 3]

def test_fill_dp():
    numbers = [{"real_part": 1}, {"real_part": 2}, {"real_part": 1}, {"real_part": 3}]
    # numbers = [[1, 0], [2, 0], [1, 0], [3, 0]]
    up, down = initialise_dp(4)
    fill_dp(numbers, up, down)
    assert up == [1, 2, 1, 3]
    assert down == [1, 1, 2, 1]


def run_tests():
    test_create_number_list()
    test_get_number_real_part_list()
    test_get_number_fractional_part_list()
    test_to_str_list()
    test_generate_numbers_list()
    test_create_number_dict()
    test_get_number_real_part_dict()
    test_get_number_fractional_part_dict()
    test_to_str_dict()
    test_generate_numbers_dict()
    test_longest_subarray()
    test_fill_dp()


# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities

def print_numbers(numbers):
    result=""
    print("The numbers entered are:")
    for i in range(len(numbers)):
        #real_part = str(get_number_real_part_list(numbers[i]))
        #fractional_part = str(get_number_fractional_part_list(numbers[i]))
        real_part = str(get_number_real_part_dict(numbers[i]))
        fractional_part = str(get_number_fractional_part_dict(numbers[i]))
        result += f" {real_part}+{fractional_part}i\n"
    return result

def print_menu():
    print("1. Read a list of complex numbers (in z = a + bi form) from the console.")
    print("2. Display the entire list of numbers on the console.")
    print("3. Display a longest subarray of numbers that contain at most 3 distinct values.")
    print("4. Display a longest alternating subsequence, when considering each number's real part." )
    print("0. Exit the program.")

def menu():
    #numbers = generate_numbers_list(10)
    numbers = generate_numbers_dict(10)
    run_tests()
    while True:
        print_menu()
        choice= input("Enter your choice: ")
        try:
            if choice == "1":
                count=int(input(" How many complex numbers do you want to add?"))
                for _ in range(count):
                    #add_new_number_list(numbers)
                    add_new_number_dict(numbers)
            elif choice == "2":
                print(print_numbers(numbers))

            elif choice == "3":
                length,subarray=longest_subarray(numbers)
                print("The length of the longest subarray is: ", length)
                #print("Subarray:", ', '.join(to_str_list(num) for num in subarray))
                print("Subarray:", ', '.join(to_str_dict(num) for num in subarray))
            elif choice == "4":
                length,subsequence=longest_alternating_subsequence(numbers)
                print("The length of the longest alternating subsequence is: ", length)
                #print("Subsequence:", ', '.join(to_str_list(num) for num in subsequence))
                print("Subsequence:", ', '.join(to_str_dict(num) for num in subsequence))
            elif choice == "0":
                break

            else:
                print("Invalid choice. Please try again.")


        except (ValueError, TypeError) as error:
            print(error)


if __name__ == "__main__":
  menu()




