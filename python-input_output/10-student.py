#!/usr/bin/python3
"""Module defining Student class with filtered serialization.

This module provides a Student class with optional attribute filtering
during JSON serialization.
"""


class Student:
    """Represent a student with filtered serialization.

    Attributes:
        first_name (str): Student's first name.
        last_name (str): Student's last name.
        age (int): Student's age.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of Student.

        Args:
            attrs (list): List of attribute names to retrieve.
                If None, retrieve all attributes.

        Returns:
            dict: Dictionary containing requested attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__
