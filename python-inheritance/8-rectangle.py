#!/usr/bin/python3
"""Module that defines Rectangle class.

This module provides a Rectangle class that inherits from BaseGeometry
and implements width and height validation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry.

    This class represents a rectangle with validated width and height.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
