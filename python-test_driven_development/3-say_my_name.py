#!/usr/bin/python3
"""Module for printing names.

This module provides a simple function to print
a formatted name string with proper validation.
"""


def say_my_name(first_name, last_name=""):
    """Print a formatted name.

    Args:
        first_name: The first name (must be a string)
        last_name: The last name (must be a string), defaults to empty

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
