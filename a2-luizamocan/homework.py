
import random
def printmenu():
    print("1. Generate a list of n random natural numbers. Generated numbers must be between 0 and 1000")
    print("2. Search for an item in the list using Interpolation search")
    print("3. Sort the list using Exchange Sort")
    print("4. Sort the list using Shell Sort")
    print("0. Exit the program")


def generate_n_numbers(n, list_of_numbers):
    for i in range(n):
        number = random.randint(0, 1000)
        list_of_numbers.append(number)
    print(list_of_numbers)

def interpolation_search(n, list_of_numbers):
    low=0
    high=len(list_of_numbers)-1
    while low<=high and list_of_numbers[low] <= n <= list_of_numbers[high]:
        if low==high:
            if list_of_numbers[low]==n:
                return low
            return -1
        pos = low + ((n - list_of_numbers[low]) * (high - low)) // (list_of_numbers[high] - list_of_numbers[low])
        if list_of_numbers[pos] == n:
            return pos

        elif list_of_numbers[pos] < n:
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


def exchange_sort(list_of_numbers, step):
    step_count=0
    for i in range( len(list_of_numbers)-1):
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[i] > list_of_numbers[j]:
                aux=list_of_numbers[i]
                list_of_numbers[i]=list_of_numbers[j]
                list_of_numbers[j] = aux

                step_count+=1
                if step_count % step == 0:
                    print(f"After {step_count} swaps: {list_of_numbers}")

    print("The final sorted list :" ,list_of_numbers)
    return list_of_numbers

def shell_sort(list_of_numbers, step):
    step_count=0
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

                    step_count += 1
                    if step_count % step == 0:
                        print(f"After {step_count} swaps: {list_of_numbers}")

                i=i-gap
            j+=1
        gap=gap//2

    print("The final sorted list :", list_of_numbers)
    return list_of_numbers

def test():
    list_test1=[576, 30, 10 , 145, 973, 269]
    list_test2=[321, 82, 502, 230, 999]
    list_test3=[1, 478, 666, 527, 879, 65, 233, 309, 917]
    list_test4=[64, 302, 800, 3]
    assert exchange_sort(list_test1, 1) == [10, 30, 145, 269, 576,973]
    assert shell_sort(list_test4, 3) == [3, 64, 302,800]
    assert interpolation_search(30, list_test1) == 1



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

        elif option == "2":
            if ok==1:
                n = int(input("Enter the number that needs to be searched: "))
                result_interpolation_search(n, list_of_numbers)
            else:
                print("Please sort the list first")

        elif option == "3":
            print("The initial list is: ")
            print(list_of_numbers)
            step = int(input("Enter the step size "))
            exchange_sort(list_of_numbers, step)
            ok=1

        elif option == "4":
            print("The initial list is: ")
            print(list_of_numbers)
            step = int(input("Enter the step size "))
            shell_sort(list_of_numbers, step)
            ok=1





main()