#!/usr/bin/python3
'''
Module 0-read_file
Has a function that reads a text file (UTF8) and prints it to stdout
'''


def read_file(filename=""):
    '''
    function that reads a text file
    '''
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')
