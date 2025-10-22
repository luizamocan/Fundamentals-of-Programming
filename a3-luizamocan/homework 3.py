
import random
import time

def printmenu():
    print("1. Generate a list of n random natural numbers. Generated numbers must be between 0 and 1000")
    print("2. Search for an item in the list using Interpolation search")
    print("3. Sort the list using Exchange Sort")
    print("4. Sort the list using Shell Sort")
    print("5. Time the algorithms for best case")
    print("6. Time the algorithms for average case")
    print("7. Time the algorithms for worst case")
    print("0. Exit the program")


def generate_n_numbers(n, list_of_numbers):
    for i in range(n):
        number = random.randint(0, 1000)
        list_of_numbers.append(number)


def print_list_of_numbers(list_of_numbers):
    for i in range (len(list_of_numbers)):
        print (list_of_numbers[i])

def interpolation_search(target, list_of_numbers):
    low=0
    high=len(list_of_numbers)-1
    while low<=high and list_of_numbers[low] <= target <= list_of_numbers[high]:
        if low==high:
            if list_of_numbers[low]==target:
                return low
            return -1
        pos = low + ((target - list_of_numbers[low]) * (high - low)) // (list_of_numbers[high] - list_of_numbers[low])
        if list_of_numbers[pos] == target:
            return pos

        elif list_of_numbers[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def result_interpolation_search(n, list_of_numbers):
    result=interpolation_search(n, list_of_numbers)
    if result == -1:
        print("The number is not present in the list")
    else:
        print("Element found at index: ", result)


def exchange_sort(list_of_numbers):

    for i in range( len(list_of_numbers)-1):
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[i] > list_of_numbers[j]:
                aux=list_of_numbers[i]
                list_of_numbers[i]=list_of_numbers[j]
                list_of_numbers[j] = aux

    return list_of_numbers

def shell_sort(list_of_numbers):

    gap = len(list_of_numbers)//2
    while gap > 0:
        j=gap
        while j< len(list_of_numbers):
            i=j-gap
            while i>=0:
                if list_of_numbers[i+gap] > list_of_numbers[i]:
                    break
                else:
                    aux=list_of_numbers[i+gap]
                    list_of_numbers[i+gap]=list_of_numbers[i]
                    list_of_numbers[i]=aux



                i=i-gap
            j+=1
        gap=gap//2
    return list_of_numbers


def generate_complexity_case_list(size_of_the_list, complexity_case_type):
    complexity_case_list = []
    if complexity_case_type == "best":
        for value in range(size_of_the_list):
            complexity_case_list.append(value)
    elif complexity_case_type == "worst":
        for value in range(size_of_the_list, 0, -1):
            complexity_case_list.append(value)
    else:
        generate_n_numbers(size_of_the_list, complexity_case_list)
    return complexity_case_list


def time_exchange_sort(complexity_case_type):
    list_size = [500, 1000, 2000, 4000, 8000]
    for size in list_size:
        list_to_sort = generate_complexity_case_list(size, complexity_case_type)
        start_time = time.perf_counter()
        exchange_sort(list_to_sort)
        duration = time.perf_counter() - start_time
        print("List size: ", size, ", Duration: ", duration, "seconds")



def time_shell_sort(complexity_case_type):
    list_size = [500, 1000, 2000, 4000, 8000]
    for size in list_size:
        list_to_sort = generate_complexity_case_list(size, complexity_case_type)
        start_time = time.perf_counter()
        shell_sort(list_to_sort)
        duration = time.perf_counter() - start_time
        print("List size: ", size, ", Duration: ", duration, "seconds")


def time_interpolation_search(complexity_case_type):
    list_size = [500, 1000, 2000, 4000, 8000]
    for size in list_size:
        list_to_sort = generate_complexity_case_list(size, complexity_case_type)
        shell_sort(list_to_sort)

        if complexity_case_type == "best":
            target = list_to_sort[0]  # Best case: target is the first element
        elif complexity_case_type == "worst":
            target = 2000  # Set target to a number not in the list for worst case
        else:
            target = list_to_sort[size // 2]  # Average case: target is a middle element

        start_time = time.perf_counter()
        interpolation_search(target, list_to_sort)
        duration = time.perf_counter() - start_time
        print("List size: ", size, ", Duration: ", duration, "seconds")


def test():
    list_test1=[576, 30, 10 , 145, 973, 269]
    list_test2=[321, 82, 502, 230, 999]
    list_test3=[1, 478, 666, 527, 879, 65, 233, 309, 917]
    list_test4=[64, 302, 800, 3]
    list_test5=[]
    list_test6=[1, 2, 3,4,5]
    list_test7=[5,4,3,2,1]
    list_test8=[1]
    assert exchange_sort(list_test1) == [10, 30, 145, 269, 576,973]
    assert shell_sort(list_test4) == [3, 64, 302,800]
    assert interpolation_search(30, list_test1) == 1
    assert exchange_sort(list_test6) ==[1,2,3,4,5]
    assert shell_sort(list_test6) == [1,2,3,4,5]
    assert exchange_sort(list_test7) == [1,2,3,4,5]
    assert shell_sort(list_test7) == [1,2,3,4,5]
    assert exchange_sort(list_test8) == [1]
    assert shell_sort(list_test8) == [1]
    assert exchange_sort(list_test5) == []
    assert shell_sort(list_test5) == []
    assert interpolation_search(2,list_test5)== -1
    assert interpolation_search(1,list_test8)== 0



def main():
    list_of_numbers = []
    ok=0
    test()

    while True:
        printmenu()
        option = input("Choose an option ")

        if option == "0":
            break

        elif option == "1":
            n = int(input("Enter a natural number "))
            print("The generated numbers are: ")
            generate_n_numbers(n, list_of_numbers)
            print_list_of_numbers(list_of_numbers)

        elif option == "2":
            if ok==1:
                n = int(input("Enter the number that needs to be searched: "))
                result_interpolation_search(n, list_of_numbers)
            else:
                print("Please sort the list first")

        elif option == "3":
            print("The final sorted list is: ")
            exchange_sort(list_of_numbers)
            print_list_of_numbers(list_of_numbers)
            ok=1

        elif option == "4":
            print("The final sorted list is: ")
            shell_sort(list_of_numbers)
            print_list_of_numbers(list_of_numbers)
            ok=1

        elif option == "5":
            print("Timing Exchange Sort for best case:")
            time_exchange_sort("best")
            print("Timing Shell Sort for best case:")
            time_shell_sort("best")
            print("Timing Interpolation Search for best case:")
            time_interpolation_search("best")

        elif option == "6":
            print("Timing Exchange Sort for average case:")
            time_exchange_sort("average")
            print("Timing Shell Sort for average case:")
            time_shell_sort("average")
            print("Timing Interpolation Search for average case:")
            time_interpolation_search("average")


        elif option == "7":
            print("Timing Exchange Sort for worst case:")
            time_exchange_sort("worst")
            print("Timing Shell Sort for worst case:")
            time_shell_sort("worst")
            print("Timing Interpolation Search for worst case:")
            time_interpolation_search("worst")



main()