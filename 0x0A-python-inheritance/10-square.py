#!/usr/bin/python3
'''
Module 10-square

extend to BaseGeometry
contain subclass Rectangle and square
with private size.
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    inherits from Rectangle and BaseGeometry
    '''

    def __init__(self, size):
        '''
        Method inicialized with private size
        '''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
