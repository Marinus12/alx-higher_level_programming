#!/usr/bin/pyhon3

def islower(c):
    """Function checks for lowercase characters"""
    lowercase = range(97, 123)
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
