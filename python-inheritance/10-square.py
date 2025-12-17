#!/usr/bin/python3
"""Module that defines Square class.

This module provides a Square class that inherits from Rectangle
and represents a square geometric shape.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle.

    This class represents a square with validated size.

    Attributes:
        __size (int): The size of the square's sides (private).
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
