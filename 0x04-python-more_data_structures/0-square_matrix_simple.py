#!/usr/bin/python3
# 0-square_matrix_simple.py
# Arth: Mahmud


def square_matrix_simple(matrix=[]):
    c = len(matrix[0])
    r = len(matrix)
    
    m = [[(row[c] ** 2) for c in range(c)] for row in matrix]
    #m = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return m
