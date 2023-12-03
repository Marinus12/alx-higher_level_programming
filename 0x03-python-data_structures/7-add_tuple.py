#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds 2 tuples"""
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) == 0:
        tuple_a = (tuple_a[0], 0)

    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)

    a_first, a_second = tuple_a
    b_first, b_second = tuple_b

    first_result = a_first + b_first
    second_result = a_second + b_second

    new_tuple = (first_result, second_result)

    return new_tuple
