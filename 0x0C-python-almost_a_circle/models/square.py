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
        self.size = size

    def __str__(self) -> str:
        '''
        method so that it
        returns [Square] (<id>) <x>/<y> - <size>
        '''
        return '[{:s}] ({:d}) {:d}/{:d} - {:d}'.format(
            self.__class__.__name__, self.id,
            self.x, self.y,
            self.size
        )

    @property
    def size(self):
        '''getter'''
        return self.__width

    @size.setter
    def size(self, value):
        '''setter'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        self.__width = value
        self.__height = value
