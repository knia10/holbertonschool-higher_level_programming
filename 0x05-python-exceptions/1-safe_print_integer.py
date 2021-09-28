#!/usr/bin/python3
def safe_print_integer(value):
    try:  # intente imprimir el valor entero
        print('{:d}'.format(value))
        return True  # retorna verdad si es numero
    except (ValueError, TypeError):  # si sale cualquiera de estos errores
        return False  # retorne falso
