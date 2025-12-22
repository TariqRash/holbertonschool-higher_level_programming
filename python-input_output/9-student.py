#!/usr/bin/python3
"""Module defining Student class.

This module provides a Student class with JSON serialization capability.
"""


class Student:
    """Represent a student with personal information.

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

    def to_json(self):
        """Return dictionary representation of Student.

        Returns:
            dict: Dictionary containing all student attributes.
        """
        return self.__dict__
