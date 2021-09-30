#!/usr/bin/python3
''' class Rectangle that defines a rectangle'''


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Getter'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Getter'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        '''returns the rectangle area'''
        return (self.__height * self.__width)

    def perimeter(self):
        'returns the rectangle perimeter'
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        'print the rectangle with the character #'
        if self.__height == 0 or self.__width == 0:
            return 0
        return ('\n'.join(['#'*self.__width for r in range(self.__height)]))
