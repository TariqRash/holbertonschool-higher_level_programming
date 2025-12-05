#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -20]), -5)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 5, -10, 3]), 5)
        self.assertEqual(max_integer([0, -5, 10]), 10)

    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 10, 2, 3]), 10)

    def test_all_same(self):
        """Test when all elements are the same"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 2.1]), 3.2)

    def test_large_list(self):
        """Test with a large list"""
        large_list = list(range(1000))
        self.assertEqual(max_integer(large_list), 999)
