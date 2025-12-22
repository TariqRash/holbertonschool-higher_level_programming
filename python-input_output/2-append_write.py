#!/usr/bin/python3
"""Module for appending to files.

This module provides a function to append a string to a text file
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """Append string to file and return character count.

    Args:
        filename (str): Path to the file. Defaults to empty string.
        text (str): Text to append. Defaults to empty string.

    Returns:
        int: Number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
