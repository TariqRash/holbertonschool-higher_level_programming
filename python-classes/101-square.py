#!/usr/bin/python3
"""Module that defines a Square class with print capability.

This module extends the Square class to support direct printing
using the print() function. It demonstrates the use of the __str__
special method for custom string representation.
"""


class Square:
    """Represents a square that can be printed directly.

    This Square class implements the __str__ method, allowing
    instances to be printed using print(). The output matches
    the my_print() method behavior.

    Attributes:
        __size (int): The size of the square's sides (private).
        __position (tuple): The (x, y) coordinates for positioning (private).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with size and position.

        Args:
            size (int, optional): The size of the square's sides.
                Defaults to 0.
            position (tuple, optional): The (x, y) position.
                Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or position is invalid.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position of the square.

        Returns:
            tuple: The current (x, y) position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with position offset.

        If size is 0, prints an empty line. Otherwise, prints the square
        at the specified position using '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return string representation of the square.

        This method allows the square to be printed using print().
        The output is identical to calling my_print().

        Returns:
            str: The string representation of the square.
        """
        if self.__size == 0:
            return ""

        result = []
        for _ in range(self.__position[1]):
            result.append("")
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(result)
