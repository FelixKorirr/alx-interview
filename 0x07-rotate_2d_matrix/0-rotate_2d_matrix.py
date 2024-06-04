#!/usr/bin/python3
"""Rotates matrix module"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix."""
    row = len(matrix)
    column = row - 1

    for x in range(0, int(row / 2)):
        for y in range(x, column - x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[column - y][x]
            matrix[column - y][x] = matrix[column - x][column - y]
            matrix[column - x][column - y] = matrix[y][column - x]
            matrix[y][column - x] = temp
