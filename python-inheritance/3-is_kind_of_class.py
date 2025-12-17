#!/usr/bin/python3
"""Module for checking class instances including inheritance.

This module provides functionality to determine if an object
is an instance of, or inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of or inherited from specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclass.
    """
    return isinstance(obj, a_class)
