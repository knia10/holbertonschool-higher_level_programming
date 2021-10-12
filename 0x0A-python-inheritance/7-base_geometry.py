#!/usr/bin/python3
'''
Module 7-base_geometry
Has Public instance method with exception
'''


class BaseGeometry:
    '''
    with Public instance method area()
    public instance method integer_validator(self, name, value)
    '''

    def area(self):
        '''
        method area() is not implemented
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        Method that validates value
        '''
        if isinstance(value, bool):
            raise TypeError('{:s} must be an integer'.format(name))
        if not isinstance(value, int):
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
