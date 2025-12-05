#!/usr/bin/python3
"""Module for printing squares.

This module provides functionality to print
a square pattern using the # character.
"""


def print_square(size):
    """Print a square made of # characters.

    Args:
        size: The size length of the square (must be an integer >= 0)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
