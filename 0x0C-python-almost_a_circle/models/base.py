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
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        class method that writes the JSON string representation
        of list_objs to a file
        '''
        new_list = []
        if list_objs is not None:
            for iter in list_objs:
                new_list.append(cls.to_dictionary(iter))
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        '''
        returns the list of the JSON string representation
        '''
        if json_string:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        '''
        returns an instance with all attributes already set
        '''
        if cls.__name__ == 'Rectangle':
            dummy = cls(8, 9)
            dummy.update(**dictionary)
            return dummy
        if cls.__name__ == 'Square':
            dummy = cls(2)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        '''
        returns a list of instances
        '''
        filename = cls.__name__ + '.json'
        new_list = []
        try:
            with open(filename, 'r') as file:
                arg = cls.from_json_string(file.read())
            for iter, dic in enumerate(arg):
                new_list.append(cls.create(**arg[iter]))
        except:
            pass
        return new_list