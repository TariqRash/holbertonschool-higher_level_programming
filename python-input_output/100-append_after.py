#!/usr/bin/python3
"""Module for inserting text after matching lines.

This module provides a function to insert a line of text
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after lines containing search string.

    Args:
        filename (str): Name of the file to modify.
        search_string (str): String to search for in each line.
        new_string (str): String to insert after matching lines.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
