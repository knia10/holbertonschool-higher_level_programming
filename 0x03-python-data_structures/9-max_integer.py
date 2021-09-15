#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        num_max = my_list[0]
        for n in my_list:
            if n > num_max:
                num_max = n
                return num_max
    else:
        return 'None'
