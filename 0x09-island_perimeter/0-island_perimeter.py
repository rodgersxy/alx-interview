#!/usr/bin/python3
"""
0-island_perimeter
a function that returns the perimeter of the island
"""


def island_perimeter(grid):
    """
    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 1
    Returns: the perimeter of the island
    """
    perimeter = 0
    for _ in range(len(grid)):
        for y in range(len(grid[_])):
            if grid[_][y] == 1:
                if _ == 0 or grid[_ - 1][y] == 0:
                    perimeter += 1
                if y == 0 or grid[_][y - 1] == 0:
                    perimeter += 1
                if _ == len(grid) - 1 or grid[_ + 1][y] == 0:
                    perimeter += 1
                if y == len(grid[_]) - 1 or grid[_][y + 1] == 0:
                    perimeter += 1
    return (perimeter)
