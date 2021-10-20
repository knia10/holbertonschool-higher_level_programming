#!/usr/bin/python3
'''
Module base
Has a Class Base with private class attribute __nb_objects
class constructor __init__(self, id=None)
'''


class Base:
    '''
    class with class attribute and
    class constructor
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        function inicialized id or increment atribute of class
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
