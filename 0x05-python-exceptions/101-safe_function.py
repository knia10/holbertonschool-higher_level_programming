#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:  # intente retornar el punt a los args
        return (fct(*args))
    except (ZeroDivisionError, ValueError, IndexError) as error:
        # alias para errores e imprima
        stderr.write('Exception: {}\n'.format(error))
        return None
