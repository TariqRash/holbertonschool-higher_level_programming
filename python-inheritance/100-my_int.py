#!/usr/bin/python3
"""Module that defines MyInt class with inverted operators.

This module demonstrates operator overloading by creating a rebel
integer class that inverts the behavior of == and != operators.
"""


class MyInt(int):
    """Rebel integer class with inverted equality operators.

    This class inherits from int but inverts the behavior of
    the == and != operators for a rebellious twist.
    """

    def __eq__(self, other):
        """Invert equality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if NOT equal, False if equal (inverted).
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert inequality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if equal, False if NOT equal (inverted).
        """
        return super().__eq__(other)
