#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format{}.

    If a ValueError message is caught. a corresponding
    message is printed to standard error.

    Args:
        va;ue (int): The integer to print.
    Return:
        If a TypeError of ValurError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)

        return (False)
