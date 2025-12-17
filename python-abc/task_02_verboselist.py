#!/usr/bin/env python3
"""Module extending Python's list with notifications.

This module demonstrates subclassing built-in types by creating
a list that prints notifications when items are added or removed.
"""


class VerboseList(list):
    """Extended list class with operation notifications.

    This class extends Python's built-in list to print messages
    whenever items are added or removed, providing visibility
    into list operations.
    """

    def append(self, item):
        """Append an item to the list with notification.

        Args:
            item: The item to append to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with items from iterable with notification.

        Args:
            iterable: An iterable of items to add to the list.
        """
        original_length = len(self)
        super().extend(iterable)
        items_added = len(self) - original_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """Remove an item from the list with notification.

        Args:
            item: The item to remove from the list.

        Raises:
            ValueError: If item is not in the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index with notification.

        Args:
            index (int, optional): The index to pop. Defaults to -1.

        Returns:
            The item that was removed from the list.

        Raises:
            IndexError: If the list is empty or index is out of range.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
