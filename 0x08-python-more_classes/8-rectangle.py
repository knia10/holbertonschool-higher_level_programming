#!/usr/bin/python3
''' class Rectangle that defines a rectangle'''


class Rectangle:
    'Defines a rectangle'
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __del__(self):
        ''' instance of Rectangle is deleted'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

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
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
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
        'print the rectangle with any character'
        if self.__height == 0 or self.__width == 0:
            return ''
        return '\n'.join([str(self.print_symbol) * self.__width
                          for r in range(self.__height)])

    def __repr__(self):
        'representation of rectangle to recreate a new instance'
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns the biggest rectangle based on the area '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
