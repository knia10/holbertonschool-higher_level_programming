#!/usr/bin/python3
'''
Module 2-append_write
Has a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
'''


def append_write(filename="", text=""):
    '''
    function that appends a string at the end of a text file
    '''
    n_lines = 0
    with open(filename, 'a', encoding='utf-8') as file:
        n_lines = file.write(text)
    return n_lines
