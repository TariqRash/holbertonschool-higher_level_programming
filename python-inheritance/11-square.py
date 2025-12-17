#!/usr/bin/python3
"""Module that defines Square class with custom string representation.

This module provides a Square class with proper string formatting
that displays it as a Square rather than Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with custom string representation.

    This class represents a square with custom formatting.

    Attributes:
        __size (int): The size of the square's sides (private).
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return string representation of the square.

        Returns:
            str: Square description in format [Square] <size>/<size>.
        """
        return f"[Square] {self.__size}/{self.__size}"
