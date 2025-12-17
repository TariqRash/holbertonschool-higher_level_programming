#!/usr/bin/python3
"""Module for checking class inheritance.

This module provides functionality to determine if an object
is an instance of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """Check if object inherited from specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj's class inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
