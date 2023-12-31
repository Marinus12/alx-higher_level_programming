#!/usr/bin/python3
"""Define a type square."""


class Square:
    """Initialize a bew square.
    Args:
        size (int): The size of the new square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size

    def area(self):
        return (self.__size * self.__size)
