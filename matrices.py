def add_row(matrix):
    """
    >>> m = [[0, 0], [0, 0]]
    >>> add_row(m)
    [[0, 0], [0, 0], [0, 0]]
    >>> n = [[3, 2, 5], [1, 4, 7]]
    >>> add_row(n)
    [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
    >>> n
    [[3, 2, 5], [1, 4, 7]]
    """
    matrix = matrix[:]
    matrix += [[0] * len(matrix[0])]
    return matrix


def add_column(matrix):
    """
    >>> m =[[0, 0], [0, 0]]
    >>> add_column(m)
    [[0, 0, 0], [0, 0, 0]]
    >>> n = [[3, 2], [5, 1], [4, 7]]
    >>> add_column(n)
    [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
    >>> n
    [[3, 2], [5, 1], [4, 7]]
    """
    import copy
    matrix_new = copy.deepcopy(matrix)
    for i in range(len(matrix_new)):
        matrix_new[i] += [0]
    return matrix_new


def add_matrices(m1, m2):
    """
    >>> a = [[1, 2], [3, 4]]
    >>> b = [[2, 2], [2, 2]]
    >>> add_matrices(a, b)
    [[3, 4], [5, 6]]
    >>> c = [[8, 2], [3, 4], [5, 7]]
    >>> d = [[3, 2], [9, 2], [10, 12]]
    >>> add_matrices(c, d)
    [[11, 4], [12, 6], [15, 19]]
    >>> c
    [[8, 2], [3, 4], [5, 7]]
    """
    import copy
    
    new_matrix = copy.deepcopy(m1)  
    for i in range(len(m1)):
        for j in range(len(m1[i])):
                new_matrix[i][j] += m2[i][j]
    return new_matrix


def scalar_mult(s, m):
    """
    >>> a = [[1, 2], [3, 4]]
    >>> scalar_mult(3, a)
    [[3, 6], [9, 12]]
    >>> b =  [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    >>> scalar_mult(10, b)
    [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
    >>> b
    [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    import copy

    new_matrix = copy.deepcopy(m)
    for i in range(len(new_matrix)):
        for j, value in enumerate(new_matrix[i]):
            new_matrix[i][j] = value * s
    return new_matrix


def row_times_column(m1, row, m2, column):
    """
    >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
    19
    >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
    22
    >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
    43
    >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
    50
    """
    m1_row = m1[row]
    m2_col = []
    for i in m2:
        m2_col += [i[column]]
    mult_list







if __name__ == '__main__':
    import doctest
    doctest.testmod()
