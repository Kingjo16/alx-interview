#!/usr/bin/python3
'''A module for a Pascal's triangle.'''


def pascal_triangle(n):
    '''List of Triangle list reprsentig a pascal triangle.'''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for m in range(n):
        line = []
        for k in range(m + 1):
            if k == 0 or k == m:
                line.append(1)
            elif m > 0 and k > 0:
                line.append(triangle[m - 1][k - 1] + triangle[m - 1][k])
        triangle.append(line)
    return triangle
