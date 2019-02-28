"""
    Given an image represented by an N x N matrix, where each pixel is represented by an int,
    write a method to rotate the image by 90 degrees.
    Can you do this in place?
"""


def rotate_matrix_counter_clockwise(matrix):
    return [list(elem) for elem in zip(*matrix)][::-1]


def rotate_matrix_clockwise(matrix):
    return [list(elem) for elem in zip(*reversed(matrix))]


m = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]


print(rotate_matrix_clockwise(m))

print(rotate_matrix_counter_clockwise(m))