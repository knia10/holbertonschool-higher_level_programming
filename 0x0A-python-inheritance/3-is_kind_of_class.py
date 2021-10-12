#!/usr/bin/python3
'''
Module is_kind_of_class
function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
'''


def is_kind_of_class(obj, a_class):
    '''
    function return true if obj is instance of class inherited
    return false otherwise.
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
