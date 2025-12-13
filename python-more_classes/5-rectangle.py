#!/usr/bin/python3
"""Module that defines a Rectangle class with destructor.

This module demonstrates the __del__ method which is called
when an instance is deleted.
"""


class Rectangle:
    """Represents a rectangle with deletion detection.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation for printing."""
        if self.__width == 0 or self.__height == 0:
            return ""
        result = []
        for _ in range(self.__height):
            result.append("#" * self.__width)
        return "\n".join(result)

    def __repr__(self):
        """Return official string representation."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Detect instance deletion and print goodbye message."""
        print("Bye rectangle...")
