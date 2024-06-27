#!/usr/bin/python3
"""Module"""


def island_perimeter(grid):
    '''`island_perimeter` calculate the perimetr of an island

    Arg(s):
        `grid`: is a list of list of integers:
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100

    `Returns`: size of the perimeter'''
    perimeter = 0
    if (len(grid) <= 100) and (len(grid[0]) <= 100):
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                cur = grid[i][j]
                if cur == 1:
                    # left island
                    if (j > 0 and (grid[i][j-1] == 0)) or (j-1 == -1):
                        perimeter += 1
                    # right
                    if (j + 1 <= col - 1 and (grid[i][j+1] == 0)) or\
                            (j + 1 > col-1):
                        perimeter += 1
                    # Top
                    if (i > 0 and (grid[i-1][j] == 0)) or (i-1 == -1):
                        perimeter += 1
                    # Bottom
                    if (i + 1 <= row - 1 and (grid[i+1][j] == 0)) or\
                            (i + 1 > row-1):
                        perimeter += 1
    return perimeter
