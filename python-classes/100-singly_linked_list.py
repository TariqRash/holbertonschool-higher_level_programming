#!/usr/bin/python3
"""Module that defines a Node and SinglyLinkedList.

This module implements a singly linked list data structure with
automatic sorted insertion. It demonstrates advanced OOP concepts
including multiple classes working together and special methods.
"""


class Node:
    """Represents a node in a singly linked list.

    A Node contains data and a reference to the next node in the list.
    This implementation uses properties to ensure type safety.

    Attributes:
        __data (int): The data stored in this node (private).
        __next_node (Node): Reference to the next node (private).
    """

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data to store in this node.
            next_node (Node, optional): The next node in the list.
                Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in this node.

        Returns:
            int: The data value.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data for this node with validation.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node in the list.

        Returns:
            Node: The next node, or None if this is the last node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node with validation.

        Args:
            value (Node): The next node in the list.

        Raises:
            TypeError: If value is not None and not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list.

    This linked list maintains sorted order automatically. When nodes
    are inserted, they are placed in the correct position to maintain
    ascending order.

    Attributes:
        __head (Node): The first node in the list (private).
    """

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position.

        The list maintains ascending order. This method finds the
        correct position and inserts the new node there.

        Args:
            value (int): The value to insert into the list.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return string representation of the list.

        Returns:
            str: The list with one node value per line.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
