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

    length = len(list_of_integers)
    if length == 1:  # si tiene un solo elem
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)  # el mayor de los elem

    list_div = int(length / 2)  # castea list a int y la divide
    left = list_div - 1
    right = list_div + 1
    peak_list = list_of_integers[list_div]  # pico ubicado en la div de la list
    # compara el izq y der si es mas grande sera lo que retorna
    if peak_list > list_of_integers[left] and\
            peak_list > list_of_integers[list_div + 1]:
        return peak_list
    # sino si el pico es menor a lo que hay a su izq recursiv
    elif peak_list < list_of_integers[left]:
        return find_peak(list_of_integers[:list_div])
    else:  # no es ninguna de las anteriores recursiv pra la derecha del pico
        return find_peak(list_of_integers[right:])
