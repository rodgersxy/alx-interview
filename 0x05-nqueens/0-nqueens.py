#!/usr/bin/python3
"""
N queens puzzle is the challenge of placing N non-attacking queens on an
NxN chessboard. This is a program that solves the N queens problem.
"""

import sys


def printSolutions(board):
    """
    Prints the coordinates of the row and column of each queen on the board
    Args:
        board: list
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def isSafe(board, row, col):
    """
    Checks if a queen can be placed on the board
    Args:
        board: list
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQueens(board, col, n):
    """
    Solves the N queens problem
    Args:
        board: list
    """
    if col == n:
        printSolutions(board)
        return
    counter = False
    for i in range(n):
        if isSafe(board, i, col):
            board[i][col] = 1
            counter = solveNQueens(board, col + 1, n) or counter
            board[i][col] = 0
    return counter


if __name__ == "__main__":
    """
    Main function
    Take the argv from the command line:
    - nqueens N, where N is the number of queens to be placed
    """

    if not len(sys.argv) == 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for i in range(n)] for j in range(n)]
    solveNQueens(board, 0, n)
