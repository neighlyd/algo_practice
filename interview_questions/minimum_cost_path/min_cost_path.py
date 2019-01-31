"""
    Given a 2D matrix of values, you are allowed to move right or down, adding up values as you go. Find the path that
will yield the minimum value to get from top left to bottom right.

example:

[[2, 3, 4],
 [5, 9, 8],
 [7, 2, 1]]

The minimum path is 17: 2 -> 5 -> 7 -> 2 -> 1
"""


def min_cost_path(matrix, end):
    rows = len(matrix)
    height = len(matrix[0])
    for idx, val in enumerate(matrix[0]):
        if idx > 0:
            matrix[0][idx] += matrix[0][idx - 1]


    for i in range(rows):
        for j in range(height):
            # don't alter the top-left cell
            if i != 0 and j != 0:
                if i > 0 and j == 0:
                    matrix[i][j] += matrix[i-1][j]
                elif i == 0
    pass
