#!/usr/bin/python3
"""Module for computing the perimeter of an island in a grid."""


def compute_island_perimeter(matrix):
    """Calculate the perimeter of an island with no internal lakes."""
    total_perimeter = 0
    if type(matrix) != list:
        return 0
    num_rows = len(matrix)
    for row_index, current_row in enumerate(matrix):
        num_cols = len(current_row)
        for col_index, cell_value in enumerate(current_row):
            if cell_value == 0:
                continue
            adjacent_edges = (
                row_index == 0 or (
                    len(matrix[row_index - 1]) > col_index and
                    matrix[row_index - 1][col_index] == 0
                ),
                col_index == num_cols - 1 or (
                    num_cols > col_index + 1 and
                    current_row[col_index + 1] == 0
                ),
                row_index == num_rows - 1 or (
                    len(matrix[row_index + 1]) > col_index and
                    matrix[row_index + 1][col_index] == 0
                ),
                col_index == 0 or current_row[col_index - 1] == 0,
            )
            total_perimeter += sum(adjacent_edges)
    return total_perimeter
