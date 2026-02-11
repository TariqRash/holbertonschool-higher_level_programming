#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """Only allows first_name as instance attribute."""

    __slots__ = ['first_name']
