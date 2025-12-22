#!/usr/bin/python3
"""Module for JSON serialization.

This module provides a function to convert Python objects
to JSON string representation.
"""
import json


def to_json_string(my_obj):
    """Return JSON representation of an object.

    Args:
        my_obj: Python object to serialize.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
