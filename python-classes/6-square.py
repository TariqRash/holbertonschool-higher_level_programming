#!/usr/bin/python3
"""Module that defines a Square class with position.

This module presents the complete Square class with both size and
position attributes. It demonstrates how multiple attributes can
work together to create sophisticated object behavior.
"""


class Square:
    """Represents a square with size and position.

    The Square class now manages both its dimensions and its position
    in 2D space, allowing for precise control over where the square
    is rendered when printed.

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
        at the specified position using '#' characters. The position[1]
        value adds vertical offset (newlines before), and position[0]
        adds horizontal offset (spaces before each line).
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
