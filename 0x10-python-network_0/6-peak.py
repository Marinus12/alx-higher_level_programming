#!/usr/bin/python3
""" FInds a peak in a list of unsorted integers
"""


def find_peak(list_integers):
    """ Function to find a peak in a list of unsorted integers.
    """
    if not list_integers:
        return None

    left, right = 0, len(list_integers) - 1

    while left < right:
        mid = (left + right) // 2
        if list_integers[mid] > list_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_integers[left]
