#!/usr/bin/python3
"""Module for text formatting.

This module provides functionality to format text
by adding line breaks after specific punctuation marks.
"""


def text_indentation(text):
    """Print text with 2 new lines after . ? and : characters.

    Args:
        text: The text to format (must be a string)

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
