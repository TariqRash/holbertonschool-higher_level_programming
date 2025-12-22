#!/usr/bin/python3
"""Module for loading objects from JSON files.

This module provides a function to create Python objects
from JSON files.
"""
import json


def load_from_json_file(filename):
    """Create object from JSON file.

    Args:
        filename (str): Path to the JSON file to read.

    Returns:
        Python object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
