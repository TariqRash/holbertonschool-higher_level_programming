#!/usr/bin/python3
"""Module for JSON deserialization.

This module provides a function to convert JSON strings
to Python objects.
"""
import json


def from_json_string(my_str):
    """Return Python object from JSON string.

    Args:
        my_str (str): JSON string to deserialize.

    Returns:
        Python object represented by the JSON string.
    """
    return json.loads(my_str)
