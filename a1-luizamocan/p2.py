# Solve the problem from the second set here
#Find the smallest number m from the Fibonacci sequence,
# defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2], for n > 2, larger than the given natural number n. (e.g. for n = 6, m = 8).

#the function generates the Fibonacci sequence until it finds the first number larger than the given natural number n
def fibonacci_number(n: int)->int:
    if n < 1:
        return 1
    x=1
    y=1
    m=x+y
    while m<=n:
        x=y
        y=m
        m=x+y
    return m

#if n is a natural number , then it returns the result, otherwise if returns a message
def fibonacci_number_larger_then_n(n: int) :
    if n<0:
        return "Please enter a natural number"
    else:
        return fibonacci_number(n)


def main():
    try:
        n = int(input("Enter a natural number: "))
        print(fibonacci_number_larger_then_n(n))
    except ValueError:
        print("Please enter a natural number")

main()