#!/usr/bin/python3
"""Module for adding two integers.

This module provides a function to add two numbers together.
It handles both integers and floats, with proper type checking
and conversion to ensure reliable integer arithmetic.
"""


def add_integer(a, b=98):
    """Add two integers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98

    Returns:
        The sum of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and (a != a):  # NaN check
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b):  # NaN check
        raise TypeError("b must be an integer")
    if isinstance(a, float) and abs(a) == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if isinstance(b, float) and abs(b) == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    return int(a) + int(b)
