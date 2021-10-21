#!/usr/bin/python3
'''
Module rectangle
Has a class Rectangle that inherits from Base
Rectangle contains Private instance attributes,
each with its own public getter and setter
'''

from models.base import Base


class Rectangle(Base):
    '''
    Class Rectangle inherits from Base
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Class constructor
        Call the super class with id - this super call with
        use the logic of the __init__ of the Base class
        Assign each argument width, height, x and y to the right attribute
        validation of all setter methods and instantiation
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''getter'''
        return self.__width

    @property
    def height(self):
        '''getter'''
        return self.__height

    @property
    def x(self):
        '''getter'''
        return self.__x

    @property
    def y(self):
        '''getter'''
        return self.__y

    @width.setter
    def width(self, input):
        '''setter'''
        if type(input) is not int:
            raise TypeError('width must be an integer')
        if input <= 0:
            raise ValueError('width must be > 0')
        self.__width = input

    @height.setter
    def height(self, input):
        '''setter'''
        if type(input) is not int:
            raise TypeError('height must be an integer')
        if input <= 0:
            raise ValueError('height must be > 0')
        self.__height = input

    @x.setter
    def x(self, input):
        '''setter'''
        if type(input) is not int:
            raise TypeError('x must be an integer')
        if input < 0:
            raise ValueError('x must be >= 0')
        self.__x = input

    @y.setter
    def y(self, input):
        '''setter'''
        if type(input) is not int:
            raise TypeError('y must be an integer')
        if input < 0:
            raise ValueError('y must be >= 0')
        self.__y = input

    def area(self):
        '''
        public method that returns area value of the Rectangle instance.
        '''
        return self.__width * self.__height

    def display(self):
        '''
        public method prints in stdout the Rectangle instance with
        the character #
        '''
        print('\n' * self.__y +
              '\n'.join([' ' * self.__x + '#' * self.__width for r in range(self.__height)]))

    def __str__(self) -> str:
        return '[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.__class__.__name__, self.id,
            self.__x, self.__y,
            self.__width, self.__height
        )
