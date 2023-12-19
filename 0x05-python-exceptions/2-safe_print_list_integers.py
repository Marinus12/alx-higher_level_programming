#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first element of a list that are integers

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    ren = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ren += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ren)
