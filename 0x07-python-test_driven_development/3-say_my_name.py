#!/usr/bin/python3
'''
Module 3-say_my_name
Has a function that  prints My name is <first name> <last name>
Receives 2 strings
'''


def say_my_name(first_name, last_name=""):
    '''
    function that prints My name is <first name> <last name>
    '''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        print('My name is {:s} {:s}'.format(last_name, first_name))
