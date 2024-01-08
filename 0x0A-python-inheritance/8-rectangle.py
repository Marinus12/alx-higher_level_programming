#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a new rectangle.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle.
        """
        swlf.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
