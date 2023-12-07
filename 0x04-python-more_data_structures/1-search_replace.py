#!/usr/bin/python3
def search_replace(my_list, serach, replace):
    return [replace if search == n else n for n in my_list]
