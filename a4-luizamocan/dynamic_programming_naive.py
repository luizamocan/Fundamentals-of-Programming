#4. Given an n * n square matrix with integer values, find the maximum length of a snake sequence.
# A snake sequence begins on the matrix's top row (coordinate (0, i), 0 <= i < n).
# Each element of the sequence, except the first one, must have a value ±1 from the previous one and be located directly below, or directly to the right of the previous element.
# For example  , element (i, j) can be succeded by one of the (i, j + 1) or (i + 1, j) elements.
#Display the length as well as the sequence of coordinates for one sequence of maximum length.

def is_in_matrix(matrix,i,j):
    n=len(matrix)
    if 0<=i<n and 0<=j<n:
        return True
    return False

def can_extend_sequence(matrix, current, neighbor):
    if abs(matrix[current[0]][current[1]] - matrix[neighbor[0]][neighbor[1]]) == 1:
        return True
    return False

def longest_snake_from_cell(matrix,i,j):
    # If out of bounds, return a path length of 0
    if not is_in_matrix(matrix,i,j):
        return 0, []

    # Initial length and path starting from this cell
    max_length = 1
    max_path = [(i, j)]

    # Check the right neighbor
    if is_in_matrix(matrix, i, j + 1) and can_extend_sequence(matrix, (i, j), (i, j + 1)):
        length, path = longest_snake_from_cell(matrix, i, j + 1)
        if length + 1 > max_length:
            max_length = length + 1
            max_path = [(i, j)] + path

    # Check the bottom neighbor
    if is_in_matrix(matrix, i + 1, j) and can_extend_sequence(matrix, (i, j), (i + 1, j)):
        length, path = longest_snake_from_cell(matrix, i + 1, j)
        if length + 1 > max_length:
            max_length = length + 1
            max_path = [(i, j)] + path

    return max_length, max_path


def find_longest_snake_sequence_naive(matrix):
    max_length = 0
    max_sequence = []

    # Try starting from each cell in the top row
    for j in range(len(matrix)):
        length, sequence = longest_snake_from_cell(matrix, 0, j)
        if length > max_length:
            max_length = length
            max_sequence = sequence

    return max_length, max_sequence

def test_find_max_snake_sequence_naive():
    matrix1 = [
        [9, 6, 5, 2],
        [8, 7, 6, 5],
        [7, 3, 1, 6],
        [1, 1, 1, 7]
    ]
    len1, seq1 = find_longest_snake_sequence_naive(matrix1)
    assert len1 == 7
    assert seq1 == [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]

    matrix2 = [
        [1, 3],
        [4, 6]
    ]
    len2, seq2 = find_longest_snake_sequence_naive(matrix2)
    assert len2 == 1
    assert seq2 in [[(0, 0)], [(0, 1)], [(1, 0)], [(1, 1)]]


    matrix3 = [
        [1]
    ]
    len3, seq3 = find_longest_snake_sequence_naive(matrix3)
    assert len3 == 1
    assert seq3 == [(0, 0)]

    matrix4 = [
        [2, 2],
        [2, 2]
    ]
    len4, seq4 = find_longest_snake_sequence_naive(matrix4)
    assert len4 == 1
    assert seq4 in [[(0, 0)], [(0, 1)], [(1, 0)], [(1, 1)]]

def main():
    test_find_max_snake_sequence_naive()
    matrix = [
        [9, 6, 5, 2],
        [8, 7, 6, 5],
        [7, 3, 1, 6],
        [1, 1, 1, 7]
    ]
    length, sequence = find_longest_snake_sequence_naive(matrix)
    print("Maximum Length of Snake Sequence (Naive):", length)
    print("Snake Sequence Coordinates (Naive):", sequence)

main()
