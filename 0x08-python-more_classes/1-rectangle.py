#!/usr/bin/python3
''' class Rectangle that defines a rectangle'''


class Rectangle:
    '''Defines a rectangle'''
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        '''Getter'''
        return self._width

    @width.setter
    def width(self, value):
        '''Setter'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self._width = value

    @property
    def height(self):
        '''Getter'''
        return self._height

    @height.setter
    def height(self, value):
        '''Setter'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self._height = value
