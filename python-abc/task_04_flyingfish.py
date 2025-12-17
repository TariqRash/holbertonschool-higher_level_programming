#!/usr/bin/env python3
"""Module demonstrating multiple inheritance with FlyingFish.

This module shows how to use multiple inheritance and understand
method resolution order (MRO) in Python.
"""


class Fish:
    """Fish class with swimming and habitat methods.

    Represents a fish that can swim and lives in water.
    """

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Bird class with flying and habitat methods.

    Represents a bird that can fly and lives in the sky.
    """

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class inheriting from both Fish and Bird.

    Demonstrates multiple inheritance by combining behaviors
    from both parent classes with custom overrides.
    """

    def swim(self):
        """Override swim method with flying fish specific message."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly method with flying fish specific message."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat method for flying fish.

        Flying fish live in both environments.
        """
        print("The flying fish lives both in water and the sky!")
