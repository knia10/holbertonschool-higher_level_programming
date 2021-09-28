#!/usr/bin/python3
def safe_print_division(a, b):
    try:  # intente dividir
        div = a / b
    except (ZeroDivisionError):
        div = None
    finally:
        # si o si mostrara el resultado aunque salga error
        print('Inside result: {}'.format(div))
    return div
