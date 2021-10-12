#!/usr/bin/python3
'''
Module 1-my_list
Has a class MyList that inherits from list
'''


class MyList(list):
    '''
    class that inherits from list
    '''

    def print_sorted(self):
        '''
        method that prints the list, but ascending sort
        '''
        print(sorted(self))
