#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Function that replaces an element in a list at a specific poistion
    without modifying the original list
    """
    copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
