#!/usr/bin/python3
'''
Module 0-add_integer
Has a function that returns the sum of two int
Receives 2 values of type int or float,changes it to int and returns the sum.
'''


def add_integer(a, b=98):
    '''
    function that adds 2 integers,and return add
    '''
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if a is float:
        a = int(a)
    if b is float:
        b = int(b)
    else:
        return a + b
