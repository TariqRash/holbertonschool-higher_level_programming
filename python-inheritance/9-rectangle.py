#!/usr/bin/python3
"""Module that defines Rectangle class with area implementation.

This module provides a complete Rectangle class with area calculation
and string representation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with full implementation.

    This class represents a rectangle with validated dimensions,
    area calculation, and string representation.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle.

        Returns:
            str: Rectangle description in format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
