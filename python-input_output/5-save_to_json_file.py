#!/usr/bin/python3
"""Module for saving objects to JSON files.

This module provides a function to write Python objects
to files using JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Write object to text file using JSON representation.

    Args:
        my_obj: Python object to save.
        filename (str): Path to the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
