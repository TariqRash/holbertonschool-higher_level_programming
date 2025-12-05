#!/usr/bin/python3
"""Module for matrix multiplication.

This module provides functionality to multiply two matrices
using pure Python with comprehensive validation.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: First matrix (list of lists of integers/floats)
        m_b: Second matrix (list of lists of integers/floats)

    Returns:
        A new matrix representing the product of m_a and m_b

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   contains non-numeric elements, or has inconsistent row sizes
        ValueError: If m_a or m_b is empty or matrices can't be multiplied
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_size_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_size_a:
            raise TypeError("each row of m_a must be of the same size")

    row_size_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_size_b:
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)

    return result
