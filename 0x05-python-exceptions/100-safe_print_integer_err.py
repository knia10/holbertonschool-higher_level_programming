#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    try:  # intente
        print('{:d}'.format(value))
        # mostrar el valor y retornar verdadero
        return True
    except (ValueError, TypeError) as error:  # en caso de error alias para ambos
        stderr.write('Exception: {}\n'.format(error))
        # escriba el error
        return False
