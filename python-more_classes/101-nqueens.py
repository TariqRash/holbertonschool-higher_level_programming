#!/usr/bin/python3
"""N Queens puzzle solver.

This module solves the N Queens problem using backtracking.
The N Queens puzzle involves placing N chess queens on an N×N
chessboard so that no two queens threaten each other.
"""
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed at board[row][col].

    Args:
        board (list): Current state of the board.
        row (int): Row to check.
        col (int): Column to check.
        n (int): Size of the board.

    Returns:
        bool: True if position is safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n, row, board, solutions):
    """Recursively solve the N Queens problem.

    Args:
        n (int): Size of the board.
        row (int): Current row being processed.
        board (list): Current board state.
        solutions (list): List to store all solutions.
    """
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)


def nqueens(n):
    """Solve the N Queens problem and print all solutions.

    Args:
        n (int): The size of the chessboard (n×n).
    """
    board = [-1] * n
    solutions = []
    solve_nqueens(n, 0, board, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
