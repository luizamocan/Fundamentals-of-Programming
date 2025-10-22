# Solve the problem from the first set here
#Generate the first prime number larger than a given natural number n.

#the function tells if a number is prime or not
def prime_number(n: int )->bool:
    if n<=1:
        return False
    if n==2:
        return True
    if n%2 ==0:
        return False
    for i in range (3, n//2+1, 2):
        if n % i == 0:
            return False
    return True

#the function finds the first prime number larger than a given natural number n
def first_prime(n:int )->int:
    n=n+1
    while not prime_number(n):
        n=n+1
    return n

#if n is a natural number , then it returns the result, otherwise if returns a message
def first_primenumber_largerthenn(n: int ):
    if n<0:
        return "Please input a natural number"
    else:
        return first_prime(n)

def main():

    try:
        n = int(input("Enter a natural number: "))
        print(first_primenumber_largerthenn(n))
    except ValueError:
        print("Please enter a natural number")
main()




