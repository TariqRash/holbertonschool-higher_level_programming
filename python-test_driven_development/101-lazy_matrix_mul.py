#!/usr/bin/python3
"""Module for lazy matrix multiplication using NumPy.

This module provides functionality to multiply two matrices
using the optimized NumPy library.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a: First matrix (list of lists of integers/floats)
        m_b: Second matrix (list of lists of integers/floats)

    Returns:
        A NumPy array representing the product of m_a and m_b
    """
    return np.dot(m_a, m_b)
