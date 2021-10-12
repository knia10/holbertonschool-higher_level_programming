#!/usr/bin/python3
'''
Module 1-write_file
has a function that writes a string to a text file (UTF8)
and returns the number of characters written
'''


def write_file(filename="", text=""):
    '''
    Function that returns the number
    of characters written
    '''
    n_lines = 0
    with open(filename, 'w', encoding='utf-8') as file:
        n_lines = file.write(text)
    return n_lines
