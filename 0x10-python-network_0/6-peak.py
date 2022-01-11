#!/usr/bin/python3
'''
Write a function that finds a peak in a list of unsorted integers.
'''


def find_peak(list_of_integers):
    '''
    function that finds a peak in a list of unsorted integers.
    '''
    if list_of_integers == [] or list_of_integers is None:
        return None

    if len(list_of_integers) == 2:
        return max(list_of_integers)

    if len(list_of_integers) > 0:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
