#!/usr/bin/env python3
"""Module demonstrating mixins with Dragon class.

This module shows how to use mixins to compose behavior
in a modular and reusable way.
"""


class SwimMixin:
    """Mixin class providing swimming capability.

    This mixin can be added to any class to give it
    the ability to swim.
    """

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying capability.

    This mixin can be added to any class to give it
    the ability to fly.
    """

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class composed from mixins.

    Demonstrates mixin composition by inheriting swimming
    and flying abilities from separate mixin classes.
    """

    def roar(self):
        """Print that the dragon roars.

        A dragon-specific method in addition to inherited
        mixin behaviors.
        """
        print("The dragon roars!")
