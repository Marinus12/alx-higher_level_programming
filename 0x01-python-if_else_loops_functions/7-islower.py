#!/usr/bin/pyhon3

def islower(c):
    """Function checks for lowercase characters"""
    lowercase = range(97, 123)
    if ord(c) in lowercase:
        return True
    else:
        return False
