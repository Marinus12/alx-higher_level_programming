#!/usr/bin/python3
def search_replace(my_list, serach, replace):
    return list(map(lambda e: replace if e == search else e, my_list))
