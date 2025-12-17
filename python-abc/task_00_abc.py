#!/usr/bin/env python3
"""Module demonstrating abstract base classes.

This module shows how to create abstract classes that enforce
method implementation in subclasses using Python's ABC package.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals.

    This class defines the interface that all animal subclasses
    must implement, specifically the sound method.
    """

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes.

        This is an abstract method that must be implemented
        by all concrete subclasses.

        Returns:
            str: The sound the animal makes.
        """
        pass


class Dog(Animal):
    """Dog class that implements the Animal interface.

    A concrete implementation of Animal representing a dog.
    """

    def sound(self):
        """Return the sound a dog makes.

        Returns:
            str: The string "Bark".
        """
        return "Bark"


class Cat(Animal):
    """Cat class that implements the Animal interface.

    A concrete implementation of Animal representing a cat.
    """

    def sound(self):
        """Return the sound a cat makes.

        Returns:
            str: The string "Meow".
        """
        return "Meow"
