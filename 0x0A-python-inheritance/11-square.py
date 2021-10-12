#!/usr/bin/python3
'''
Module 11-square

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

    def __str__(self) -> str:
        '''
        print square area
        '''
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__size, self.__size)
