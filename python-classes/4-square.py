#!/usr/bin/python3
"""Module that defines a Square class with property accessors.

This module demonstrates the Pythonic way of implementing getters
and setters using the @property decorator. This approach provides
controlled access to private attributes while maintaining clean syntax.
"""


class Square:
    """Represents a square with property-based attribute access.

    The Square class uses Python properties to provide controlled access
    to the private size attribute. This allows validation on both getting
    and setting the size while maintaining a clean, Pythonic interface.

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
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
