#!/usr/bin/python3
def safe_print_integer(value):
    """Print all integers with "{:d}".format().

    Args:
        value (int): The iteger to print
    Return:
        If a TypeError or ValueError occure - False.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
