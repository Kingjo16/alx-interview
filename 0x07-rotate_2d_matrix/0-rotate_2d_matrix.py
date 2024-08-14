#!/usr/bin/python3
"""Module for 2D rotation matrix."""


def rotate_2d_matrix(matrix):
    """Rotates a sd matrix by given variable."""
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    given_rows = len(matrix)
    given_cols = len(matrix[0])
    if not all(map(lambda x: len(x) == given_cols, matrix)):
        return
    gc, gr = 0, given_rows - 1
    for ind in range(given_cols * given_rows):
        if ind % given_rows == 0:
            matrix.append([])
        if gr == -1:
            gr = given_rows - 1
            gc += 1
        matrix[-1].append(matrix[gr][gc])
        if gc == given_cols - 1 and gr >= -1:
            matrix.pop(gr)
        gr -= 1
