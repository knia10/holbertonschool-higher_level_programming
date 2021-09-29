#!/usr/bin/python3
''' class Square that defines a square'''


class Square:
    '''Define initial state of attribute'''

    def __init__(self, size=0):
        '''Private instance attribute'''
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    '''Public instance method'''

    def area(self):
        ''' returns the current square area'''
        return (self.__size)**2
