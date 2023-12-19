#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists elements by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Return:
        A new list of length list_length containing all the divisions.
    """
    list_new = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division to 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            list_new.append(div)
    return (list_new)
