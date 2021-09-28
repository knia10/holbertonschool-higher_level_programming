#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elem = 0
    while elem < x:
        try:  # intente hacer
            print('{}'.format(my_list[elem]), end='')
            # mostrar cada elemento de la lista ^
        except IndexError:  # si encuentra este error pare y aumente elemt
            break
        elem += 1
    print('')
    return elem
