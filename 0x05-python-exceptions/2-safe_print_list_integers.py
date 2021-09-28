#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    countint = 0  # contador de enteros
    for pos in range(x):
        try:  # intente
            print('{:d}'.format(my_list[pos]), end='')
            # mostrar los enteros que hay en cada posicion ^
            countint += 1
        except (ValueError, TypeError):
            continue  # si encuentra estos errores
    print('')  # imprime espacio
    return countint
