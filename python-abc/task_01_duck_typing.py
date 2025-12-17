#!/usr/bin/env python3
"""Module demonstrating duck typing with shapes.

This module implements abstract Shape class and concrete implementations
using duck typing principles for flexible polymorphism.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes.

    Defines the interface for calculating area and perimeter
    that all shape subclasses must implement.
    """

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """Circle shape implementation.

    Represents a circle with a given radius and implements
    area and perimeter calculations.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """Initialize a Circle with given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = abs(radius)

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area (π * r²).
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter (2 * π * r).
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape implementation.

    Represents a rectangle with given width and height and
    implements area and perimeter calculations.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle with given dimensions.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            float: The area (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter (2 * (width + height)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape using duck typing.

    This function demonstrates duck typing by accepting any object
    that implements the Shape interface (has area and perimeter methods).

    Args:
        shape: Any object with area() and perimeter() methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
