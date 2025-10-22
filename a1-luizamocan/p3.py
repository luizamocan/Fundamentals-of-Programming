# Solve the problem from the third set here
#Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, a message should be displayed.
# A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number, as 6=1+2+3)

#the function calculates the sum of the divisors of the number n, except itself
def sum_of_divisors(n: int)->int:
    s=0
    for i in range(1,n//2+1):
        if n % i == 0:
            s+=i
    return s

#the function tells if a natural number n is perfect or not
def perfect_number(n:int )->bool:
    result=False
    if sum_of_divisors(n)==n:
        result=True
    return result


#if n is a natural number and there is a perfect number smaller, then it returns that number, otherwise if returns a message
def largest_perfect_number(n:int):
    if n>0:
        n=n-1
        while perfect_number(n)==False :
            n=n-1
        if n>1:
            return n
        else:
            return "There is no perfect number smaller than n"
    else:
        return "Please enter a natural number"



def main():
    try:
        n=int(input("Enter a natural number: "))
        print(largest_perfect_number(n))
    except ValueError:
        print("Please enter a natural number")


main()
