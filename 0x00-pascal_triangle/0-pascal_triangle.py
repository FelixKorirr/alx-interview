#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """Create a function that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    result = []
    if n > 0:
        for x in range(1, n + 1):
            level = []
            C = 1
            for y in range(1, x + 1):
                level.append(C)
                C = C * (x - y) // y
            result.append(level)
    return result
