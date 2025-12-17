#!/usr/bin/python3
"""Module that defines MyList class inheriting from list.

This module demonstrates inheritance by creating a custom list class
that adds a method to print the list in sorted order.
"""


class MyList(list):
    """Custom list class with sorted printing capability.

    Inherits from the built-in list class and adds a method
    to print the list contents in ascending order without
    modifying the original list.
    """

    def print_sorted(self):
        """Print the list in ascending sorted order.

        Creates a sorted copy of the list and prints it.
        The original list remains unchanged.
        """
        print(sorted(self))
