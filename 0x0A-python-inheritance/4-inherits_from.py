#!/usr/bin/python3
'''
Module inherits_from
Has a function that returns True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class ; otherwise False.
'''


def inherits_from(obj, a_class):
    '''
    function that returns True if the obj is an subclass
    otherwise return False.
    '''
    if type(obj) is not a_class and issubclass(
            type(obj), a_class):  # directo type, indirecto sub
        return True
    else:
        return False
