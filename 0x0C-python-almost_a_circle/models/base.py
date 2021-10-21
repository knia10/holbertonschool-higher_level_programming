#!/usr/bin/python3
'''
Module base
Has a Class Base with private class attribute __nb_objects
class constructor __init__(self, id=None)
'''
import json

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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        returns the JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None or list_dictionaries[0] == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)