#4. Given an n * n square matrix with integer values, find the maximum length of a snake sequence.
# A snake sequence begins on the matrix's top row (coordinate (0, i), 0 <= i < n).
# Each element of the sequence, except the first one, must have a value ±1 from the previous one and be located directly below, or directly to the right of the previous element.
# For example  , element (i, j) can be succeded by one of the (i, j + 1) or (i + 1, j) elements.
#Display the length as well as the sequence of coordinates for one sequence of maximum length.
def initialize_dp_and_parent(n):
    dp=[]
    parent=[]
    for i in range(n):
        dp_row=[]
        parent_row=[]
        for j in range(n):
            dp_row.append(1)
            parent_row.append(None)
        dp.append(dp_row)
        parent.append(parent_row)
    return dp,parent

def update_dp_and_parent(matrix,dp,parent,i,j):
#check the top neighbor
     if i>0 and abs(matrix[i][j]-matrix[i-1][j])==1:
         if dp[i][j]<dp[i-1][j]+1:
             dp[i][j]=dp[i-1][j]+1
             parent[i][j]=(i-1,j)

#check the left neighbor
     if j>0 and abs(matrix[i][j]-matrix[i][j-1])==1:
         if dp[i][j]<dp[i][j-1]+1:
             dp[i][j]=dp[i][j-1]+1
             parent[i][j]=(i,j-1)

def max_length_and_end_cell(dp):
    #Find  the  maximum length of snake sequence and its ending cell.
    max_len=0
    end_cell=(0,0)
    for i in range(len(dp)):
        for j in range(len(dp)):
            if dp[i][j]>max_len:
                max_len=dp[i][j]
                end_cell=(i,j)
    return max_len,end_cell

def trace_back_sequence(parent, end_cell):
    sequence=[]
    while end_cell:
        sequence.append(end_cell)
        end_cell=parent[end_cell[0]][end_cell[1]]
    sequence.reverse() # to get the elements in the correct order
    return sequence


def find_max_snake_sequence(matrix):
    n=len(matrix)
    dp,parent=initialize_dp_and_parent(n)

    for i in range(n):
        for j in range(n):
            update_dp_and_parent(matrix,dp,parent,i,j)

    max_len,end_cell=max_length_and_end_cell(dp)
    sequence=trace_back_sequence(parent,end_cell)
    return max_len,sequence


def test_find_max_snake_sequence():
    matrix1 = [
        [9, 6, 5, 2],
        [8, 7, 6, 5],
        [7, 3, 1, 6],
        [1, 1, 1, 7]
    ]
    len1, seq1 = find_max_snake_sequence(matrix1)
    assert len1 == 7
    assert seq1 == [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]

    matrix2 = [
        [1, 3],
        [4, 6]
    ]
    len2, seq2 = find_max_snake_sequence(matrix2)
    assert len2 == 1
    assert seq2 in [[(0, 0)], [(0, 1)], [(1, 0)], [(1, 1)]]


    matrix3 = [
        [1]
    ]
    len3, seq3 = find_max_snake_sequence(matrix3)
    assert len3 == 1
    assert seq3 == [(0, 0)]

    matrix4 = [
        [2, 2],
        [2, 2]
    ]
    len4, seq4 = find_max_snake_sequence(matrix4)
    assert len4 == 1
    assert seq4 in [[(0, 0)], [(0, 1)], [(1, 0)], [(1, 1)]]

def main():
    test_find_max_snake_sequence()
    matrix = [
        [9, 6, 5, 2],
        [8, 7, 6, 5],
        [7, 3, 1, 6],
        [1, 1, 1, 7]
    ]
    length, sequence = find_max_snake_sequence(matrix)
    print("Maximum Length of Snake Sequence:", length)
    print("Snake Sequence Coordinates:", sequence)
main()

