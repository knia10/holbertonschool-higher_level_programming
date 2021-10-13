#!/usr/bin/python3
'''
Module 9-student
Has a class Student
istantiation with self, first_name, last_name, age
the class contains Public method def to_json(self)
'''


class Student():
    '''
    class Student that defines a student by
    '''

    def __init__(self, first_name, last_name, age):
        '''Instantiation with first_name, last_name and age'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        retrieves a dictionary representation of a Student instance
        '''
        return self.__dict__
