#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        num_max = my_list[0]   # 1er elemento
        for n in range(0, len(my_list)):   # desde 0 hasta el final de lista
            if my_list[n] > num_max:
                num_max = my_list[n]
                return num_max
    else:
        return 'None'
