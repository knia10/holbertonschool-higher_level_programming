#!/usr/bin/python3
'''
Module 8-rectangle
Extend to BaseGeometry
with subclass Rectangle with privates attributes width, height
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Inherits fron BaseGeometry
    '''

    def __init__(self, width, height):
        '''
        width and height must be positive integers,
        validated by integer_validator
        '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', width)
        self.__height = height

    def area(self):
        '''
        Inheried of superclass for return area
        '''
        return self.__width * self.__height

    def __str__(self) -> str:
        '''
        print area and result
        '''
        return '[{:s}] {:d}/{:d}'.format(self.__class__.__name__,
                                         self.__width, self.__height)
