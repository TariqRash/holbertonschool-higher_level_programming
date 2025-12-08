#!/usr/bin/python3
"""Module that defines a Square class with size.

This module demonstrates the concept of private attributes in Python.
The Square class encapsulates a size attribute that is kept private
to maintain control over its access and modification.
"""


class Square:
    """Represents a square with a private size attribute.

    The size is stored as a private instance attribute to ensure
    encapsulation and control over the square's dimensions.

    Attributes:
        __size (int): The size of the square's sides.
    """

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square's sides.
        """
        self.__size = size
