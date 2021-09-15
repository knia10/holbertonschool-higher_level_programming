#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_ta = len(tuple_a)
    len_tb = len(tuple_b)
    sumt = ((tuple_a[0] if len_ta > 0 else 0) + (tuple_b[0] if len_tb > 0 else 0),
            (tuple_a[1] if len_ta > 0 else 0) + (tuple_b[1] if len_tb > 1 else 0))
    return sumt
