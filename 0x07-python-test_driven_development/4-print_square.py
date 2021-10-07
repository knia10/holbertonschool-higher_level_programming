#!/usr/bin/python3
'''
Module 4-print_square
Has a function that prints a square with the character #.
The size must be an integer
'''


def print_square(size):
    '''
    function that prints a square with the character #
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size is float and size < 0:
        raise TypeError('size must be an integer')
    if size == 0:
        print('', end='')
    else:
        print('\n'.join(['#' * size for row in range(size)]))
