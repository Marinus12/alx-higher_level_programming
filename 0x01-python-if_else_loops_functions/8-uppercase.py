#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            upper_case = chr(ord(char) - ord('a') + ord('A'))
        else:
            upper_case = char

        print("{}".format(upper_case), end="")
    print()
