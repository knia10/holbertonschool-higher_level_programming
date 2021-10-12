#!/usr/bin/python3
'''
Module 0-lookup
Has a function that returns the list of available attributes
and methods of an object
'''


def lookup(obj):
    '''
    function that returns the list of available attributes
    and methods of an object
    '''
    return(dir(obj))
