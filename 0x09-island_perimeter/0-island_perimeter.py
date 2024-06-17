#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    k = len(grid)
    for x, row in enumerate(grid):
        l = len(row)
        for y, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                x == 0 or (len(grid[x - 1]) > y and grid[x - 1][y] == 0),
                y == l - 1 or (l > y + 1 and row[y + 1] == 0),
                x == k - 1 or (len(grid[x + 1]) > y and grid[x + 1][y] == 0),
                y == 0 or row[y - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
