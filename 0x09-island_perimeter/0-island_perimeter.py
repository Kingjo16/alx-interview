#!/usr/bin/python3
"""Module for computing the perimeter of an island in a grid."""


def island_perimeter(g):
    """Calculate the perimeter of an island with no internal lakes."""
    p = 0
    if type(g) != list:
        return 0
    n = len(g)
    for i, r in enumerate(g):
        m = len(r)
        for j, c in enumerate(r):
            if c == 0:
                continue
            e = (
                i == 0 or (len(g[i - 1]) > j and g[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and r[j + 1] == 0),
                i == n - 1 or (len(g[i + 1]) > j and g[i + 1][j] == 0),
                j == 0 or r[j - 1] == 0,
            )
            p += sum(e)
    return p
