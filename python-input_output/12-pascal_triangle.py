#!/usr/bin/python3
"""Module for generating Pascal's triangle.

This module provides a function to generate Pascal's triangle
of any size n.
"""


def pascal_triangle(n):
    """Generate Pascal's triangle of size n.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: List of lists representing Pascal's triangle.
              Empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle
