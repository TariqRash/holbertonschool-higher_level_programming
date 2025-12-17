#!/usr/bin/python3
"""Module that provides dynamic attribute addition functionality.

This module contains a function to safely add attributes to objects
that support dynamic attribute assignment.
"""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if possible.

    This function attempts to add a new attribute to an object.
    It checks if the object supports dynamic attribute addition
    by verifying the presence of __dict__.

    Args:
        obj: The object to add the attribute to.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object doesn't support new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
