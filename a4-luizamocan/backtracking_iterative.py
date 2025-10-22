#The sequence a = a1, ..., an with integer elements is given.
# Determine all strictly increasing subsequences of sequence a (conserve the order of elements in the original sequence).
#iterative
def solution_found(subsequence):
    print("Solution:", subsequence)

def bkt_iterative(a):
    n = len(a)
    for i in range(n):
        # List to hold all subsequences starting from a[i]
        subsequences = [[a[i]]]
        for subseq in subsequences:
            solution_found(subseq)  # Print the current valid subsequence

            last_elem = subseq[-1]
            for j in range(a.index(last_elem) + 1, n):
                if a[j] > last_elem:
                    new_subseq = subseq + [a[j]]
                    subsequences.append(new_subseq)



def main():
    a = [1, 2, 5,7,3,9]
    bkt_iterative(a)

main()
