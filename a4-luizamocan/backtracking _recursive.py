#The sequence a = a1, ..., an with integer elements is given.
# Determine all strictly increasing subsequences of sequence a (conserve the order of elements in the original sequence).
#recursive
def consistent(x):
    for i in range(len(x)-1):
        if x[i]>=x[i+1]:
            return False
    return True


def solution(x):
    return len(x)>0

def solution_found(x):
    print("Solution: ", x)

def bkt_rec(x, a, start):
    for i in range(start , len(a)):
        x.append(a[i]) #append the element to the sequence
        if consistent(x):
            if solution(x):
                solution_found(x)
            bkt_rec(x,a, i+1)
        x.pop() #remove the last element to continue the backtracking


def test_consistent():
    assert consistent([1,2,3,4,5])==True
    assert consistent([5]) == True
    assert consistent([5,4,3,2,1])==False
    assert consistent([])==True


def test_solution():
    assert solution([1,2,3,4,5])==True
    assert solution([5,4,3,2,1])==True
    assert solution([])==False


def main():
    test_consistent()
    test_solution()
    a=[1,2, 5, 7,3,9]
    bkt_rec([],a,0)


main()


