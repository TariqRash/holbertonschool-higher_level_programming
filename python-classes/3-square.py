#!/usr/bin/python3
"""Module that defines a Square class with area calculation.

This module builds upon previous Square implementations by adding
the ability to calculate the area of the square. It demonstrates
how methods provide behavior to classes.
"""


class Square:
    """Represents a square that can calculate its area.

    The Square class encapsulates both data (size) and behavior
    (area calculation), demonstrating core OOP principles.

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

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
