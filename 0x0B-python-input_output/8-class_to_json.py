#!/usr/bin/python3
'''
Module 8-my_class
Has a Write a function that returns the dictionary description with simple data
structure for JSON serialization of an object
'''


def class_to_json(obj):
    '''
    function that returns the dictionary
    with simple data structure (list, dictionary, string, integer and boolean)
    '''
    return obj.__dict__