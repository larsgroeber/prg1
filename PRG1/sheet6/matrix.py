"""Solution for exercise 6.1."""

import random


def print_matrix(matrix, n, m):
    """Print a matrix to the screen."""
    for i in range(n):
        result = []
        for j in range(m):
            result.append(str(matrix[i * m + j]))
        print(f'({" ".join(result)})')


def create_matrix(n, m):
    """
    Returns a random matrix of size n x m.
    Keys are integers, starting at 0 to n*m.
    Index of the cell at (i,j) is i*m+j.
    """
    if n < 2 or m < 2:
        print('n and m must not be smaller than 2!')
        exit(1)
    size = n * m
    matrix = dict()
    for i in range(size):
        j = i % 4
        value = random.randint(10 ** j, int(9.999 * 10 ** j))
        matrix[i] = value if random.random() < 0.5 else -value

    random.shuffle(matrix)

    return matrix


def format_matrix(matrix, n, m):
    """Format matrix and return it."""
    col_length = [0] * m
    # find largest length per column
    for i in range(n):
        for j in range(m):
            length = len(str(matrix[i * m + j]))
            if length > col_length[j]:
                col_length[j] = length

    # format matrix
    for i in range(n):
        for j in range(m):
            length = col_length[j]
            matrix[i * m + j] = ("{:" + str(length) + "}").format(matrix[i * m + j])

    return matrix


def transpose_matrix(matrix, n, m):
    """Returns the transposed matrix."""
    orig_matrix = matrix.copy()
    for i in range(n):
        for j in range(m):
            matrix[j * n + i] = orig_matrix[i * m + j]
    return matrix


def main():
    n = int(input('n = '))
    m = int(input('m = '))
    print('Original matrix:')
    matrix = create_matrix(n, m)
    print_matrix(matrix, n, m)
    print('Formatted matrix:')
    print_matrix(format_matrix(matrix, n, m), n, m)
    print('Transposed formatted matrix:')
    # here n and m has to be interchanged
    print_matrix(transpose_matrix(matrix, n, m), m, n)


if __name__ == '__main__':
    main()
