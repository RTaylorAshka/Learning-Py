def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    tl = []
    br = []

    for i in range(0, len(matrix)):
        m = matrix[i]
        tl.append(m[i])

    v = 0
    for i in range(len(matrix)-1, -1, -1):
        m = matrix[i]
        br.append(m[v])
        v=v+1
        

    return (sum(br) + sum(tl)) 