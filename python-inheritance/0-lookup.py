#!/usr/bin/python3
"""Module that provides object introspection functionality.

This module contains a function to retrieve all attributes and methods
of an object using Python's built-in dir() function.
"""


def lookup(obj):
    """Return list of available attributes and methods of an object.

    Args:
        obj: Any Python object to inspect.

    Returns:
        list: A list of strings representing all attributes and methods.
    """
    return dir(obj)
