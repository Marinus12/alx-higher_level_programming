#!/usr/bin/python3
"""Module composed by a function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """Function that multiplies two matrices
    Args:
        m_a: matrix a
        m_b: matrix b
    Returns:
        TypeError: if m_a or m_b isn't a list
        TypeError: if m_a or m_b isn't a list of a list
        ValueError: if m_a or m_b is empty
        TypeError: if the list of m_a or m_b don't have int or float
        TypeError: if the rows of m_a or _b don't have the same size
        ValueError: if m_a and m_b can't be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elems in m_a:
        if not isinstance(elems, list):
            raise TypeError("m_a must be a list of lists")
    if not all(isinstance(elems, list) for elems in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elems in lists:
            if not isinstance(elems, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elems in lists:
            if not isinstance(elems, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    length = 0

    for elems in m_a:
        if length != 0 and len(elems):
            raise TypeError("each row of m_a must be of the same size")
        length = len(elems)
    for elems in m_b:
        if length != 0 and len(elems):
            raise TypeError("each row of m_b must be of the same size")
        length = len(elems)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    r1 = []

    for a in m_a:
        r2 = []
        for b in zip(*m_b):
            num = sum(x * y for x, y in zip(a, b))
            r2.append(num)

        r1.append(r2)

    return r1
