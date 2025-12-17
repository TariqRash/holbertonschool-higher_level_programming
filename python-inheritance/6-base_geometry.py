#!/usr/bin/python3
"""Module that defines BaseGeometry class with area method.

This module provides a base geometry class with an unimplemented
area method that raises an exception.
"""


class BaseGeometry:
    """Base class for geometry objects with area method.

    This class defines the interface for geometry objects
    requiring an area calculation.
    """

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Always raises with message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
