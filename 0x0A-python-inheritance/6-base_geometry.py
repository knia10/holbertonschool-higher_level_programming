#!/usr/bin/python3
'''
Module base_geometry
Has Public instance method with exception
'''


class BaseGeometry:
    '''
    with Public instance method
    '''

    def area(self):
        raise Exception('area() is not implemented')
