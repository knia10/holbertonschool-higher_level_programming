#!/usr/bin/python3
'''
Module base_geometry
Has Public instance method with exception
'''


class BaseGeometry:
    '''
    with Public instance method area()
    public instance method integer_validator(self, name, value)
    '''

    def area(self):
        '''
        
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
