#!/usr/bin/python3
''' class Square that defines a square'''


class Square:
    '''Define initial state of attribute'''

    def __init__(self, size=0):
        '''inicialiced square'''
        self.size = size

    @property
    def size(self):
        '''Getter'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter'''
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    '''Public instance method'''

    def area(self):
        ''' returns the current square area'''
        return (self.__size)**2
