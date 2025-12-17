#!/usr/bin/env python3
"""Module providing iterator with counting capability.

This module demonstrates extending iterator functionality by
tracking the number of items that have been iterated over.
"""


class CountedIterator:
    """Iterator that counts items as they are iterated.

    This class wraps an iterator and keeps track of how many
    items have been fetched using the __next__ method.

    Attributes:
        iterator: The underlying iterator object.
        count (int): The number of items iterated so far.
    """

    def __init__(self, iterable):
        """Initialize CountedIterator with an iterable.

        Args:
            iterable: Any iterable object to wrap.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Fetch next item and increment counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: When there are no more items.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the current count of iterated items.

        Returns:
            int: The number of items that have been iterated.
        """
        return self.count
