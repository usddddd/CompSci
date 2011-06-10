def add_vectors(u, v):
    """
    >>> add_vectors([1, 0], [1 ,1])
    [2, 1]
    >>> add_vectors([1, 2], [1, 4])
    [2, 6]
    >>> add_vectors([1, 2, 1], [1, 4, 3])
    [2, 6, 4]
    >>> add_vectors([11, 0 , -4, 5], [2, -4, 17, 0])
    [13, -4, 13, 5]
    """

    new_list = []
    for i in range(len(u)):
        new_list += [u[i] + v[i]]
    return new_list
    

def scalar_mult(s, v):
    """
    >>> scalar_mult(5, [1 ,2])
    [5, 10]
    >>> scalar_mult(3, [1, 0, -1])
    [3, 0, -3]
    >>> scalar_mult(7, [3, 0, 5, 11, 2])
    [21, 0, 35, 77, 14]
    """
    for i,value in enumerate(v):
        v[i] = value * s
    return v

def dot_product(u, v):
    """
    >>> dot_product([1, 1], [1, 1])
    2
    >>> dot_product([1, 2], [1, 4])
    9
    >>> dot_product([1, 2, 1], [1, 4, 3])
    12
    >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
    0
    """
    new_list = []
    for i in range(len(u)):
        new_list += [u[i] * v[i]]
    return sum(new_list)


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
    return dot_product(m1_row, m2_col)


def matrix_mult(m1, m2):
    """
    >>> matrix_mult([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    >>> matrix_mult([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 1], [2, 3]])
    [[31, 19], [85, 55]]
    >>> matrix_mult([[7, 8], [9, 1], [2, 3]], [[1, 2, 3], [4, 5, 6]])
    [[39, 54, 69], [13, 23, 33], [14, 19, 24]]
    """
    m1_rows = len(m1)
    m2_cols = len(m2[0])
    product_matrix = []

    for row in range(m1_rows):
        new_row = []
        for column in range(m2_cols):
            new_row += [row_times_column(m1, row, m2, column)]
        product_matrix += [new_row]
    return product_matrix
    
def double_stuff(a_list):
    for index, value in enumerate(a_list):
        a_list[index] = value * 2


def pure_double(a_list):
    new_list = []
    for value in a_list:
        new_list += [2 * value]
    return new_list


def make_matrix(rows, columns):
    """
    >>> m = make_matrix(4, 3)
    >>> m
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    >>> m[1][2] = 7
    >>> m
    [[0, 0, 0], [0, 0, 7], [0, 0, 0], [0, 0, 0]]
    """
    matrix = []
    for row in range(rows):
        matrix += [[0] * columns]
    return matrix
        


if __name__ == "__main__":
    import doctest
    doctest.testmod()
