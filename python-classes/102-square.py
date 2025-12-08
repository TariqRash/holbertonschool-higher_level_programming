#!/usr/bin/python3
"""Module that defines a Square class with comparison operators.

This module implements a Square class that supports comparison
operations based on area. It demonstrates the use of special methods
for operator overloading in Python.
"""


class Square:
    """Represents a square that can be compared with other squares.

    This Square class implements comparison operators (__eq__, __ne__,
    __lt__, __le__, __gt__, __ge__) based on the square's area.
    This allows squares to be compared using standard Python operators.

    Attributes:
        __size (float/int): The size of the square's sides (private).
    """

    def __init__(self, size=0):
        """Initialize a new Square with validated size.

        Args:
            size (float/int, optional): The size of the square's sides.
                Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            float/int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (float/int): The new size for the square.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            float/int: The area of the square (size squared).
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square is less than another based on area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is less than or equal based on area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is greater than another based on area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equal based on area.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
