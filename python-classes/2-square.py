#!/usr/bin/python3
"""Module that defines a Square class with validated size.

This module extends the Square class to include validation for the
size attribute. It demonstrates defensive programming by ensuring
that invalid values cannot be assigned to the square's size.
"""


class Square:
    """Represents a square with validated size.

    The Square class ensures data integrity by validating the size
    attribute during initialization. Only positive integers are accepted.

    Attributes:
        __size (int): The size of the square's sides (private).
    """

    def __init__(self, size=0):
        """Initialize a new Square with validated size.

        Args:
            size (int, optional): The size of the square's sides.
                Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
