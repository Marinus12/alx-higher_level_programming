#!/usr/bin/python3
# Ukewuihe Marinus

"""Prints the numbers from 1 to 10 seperated by a space
   For multiples of three print Fizz instead of the number
   For numbers that are multiples of both 3 and 5 print FizzBuzz
   For multiples of five print Buzz instead of the number
   """


def fizzbuzz():

    for number in range(1, 101):

        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
