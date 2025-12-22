#!/usr/bin/python3
"""Module for reading and printing file contents.

This module provides a function to read a UTF-8 text file
and print its contents to standard output.
"""


def read_file(filename=""):
    """Read a text file and print to stdout.

    Args:
        filename (str): Path to the file to read. Defaults to empty string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
