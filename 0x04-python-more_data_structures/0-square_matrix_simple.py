#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """function that replaces all occurrences of
    an element by another in a new list"""

    square_val = list(map(lambda y: list(map(lambda x: x * x, y)), matrix))
    return square_val
