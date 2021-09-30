#!/usr/bin/python3
''' class Rectangle that defines a rectangle'''


class Rectangle:
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

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

    def area(self):
        '''returns the rectangle area'''
        return (self._height * self._width)

    def perimeter(self):
        'returns the rectangle perimeter'
        if self._height == 0 or self._width == 0:
            return 0
        return (self._height * 2) + (self._width * 2)
