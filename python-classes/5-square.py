#!/usr/bin/python3
"""Module that defines a Square class with printing capability.

This module extends the Square class to include visual representation.
The square can now draw itself using the '#' character, demonstrating
how objects can have methods that interact with the outside world.
"""


class Square:
    """Represents a square that can print itself.

    The Square class combines data management with visual output,
    providing a complete representation of a geometric shape that
    knows both its properties and how to display itself.

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

    def my_print(self):
        """Print the square using the '#' character.

        If size is 0, prints an empty line. Otherwise, prints a square
        pattern using '#' characters where each side has length equal to size.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
