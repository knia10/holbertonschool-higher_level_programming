#!/usr/bin/python3
'''
Module 2-matrix_divided
Has a function that divides all elements of a matrix.
Receives 2 values of type int or float,Each row must be of the same size
'''


def matrix_divided(matrix, div):
    '''
    function that divides all elements of a matrix,Returns a new matrix
    '''
    m_except = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(m_except)
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    len_matrix = len(matrix[0])
    for l in matrix:
        if type(l) is not list:
            raise TypeError(m_except)
        if len(l) != len_matrix:
            raise TypeError('Each row of the matrix must have the same size')
        new_list = []
        for idx in l:
            if not isinstance(idx, (int, float)):
                raise TypeError(m_except)
            new_list.append(round(idx/div, 2))
        new_matrix.append(new_list)
    return new_matrix
