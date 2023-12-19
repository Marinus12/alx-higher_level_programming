#!/usr/bin/python3
def safe_print_division(q, b):
    """Prints the division of a and b"""
    try:
        div = a / b
        except(TypeError, ValueError):
            div = None
        finally:
            print("Inside result: {}".format(div))
        return (div)
