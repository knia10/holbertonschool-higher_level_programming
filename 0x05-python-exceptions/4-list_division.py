#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []  # nueva lista vacia
    for i in range(list_length):
        div = 0  # cada que empieza el ciclo div se reinicia
        # para que de 0 si no se pude div
        try:  # intente dividir los elem de las list
            div = my_list_1[i] / my_list_2[i]
        except(TypeError):  # If an element is not an integer or float:
            print('wrong type')
        except (ZeroDivisionError):  # If the division can’t be done (/0):
            print('division by 0')
        except(IndexError):  # If my_list_1 or my_list_2 is too short
            print('out of range')
        finally:
            new_list.append(div)
    return new_list
