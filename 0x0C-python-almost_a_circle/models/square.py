#!/usr/bin/python3
'''
Module Square
Has a class Square that inherits from Rectangle
Square contains a Class constructor
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    inherits from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Call the super class with id, x, y, width and height
        create new atribute size.
        '''
        super().__init__(size, size, x, y, id)
