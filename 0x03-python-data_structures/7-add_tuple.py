#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lta = len(tuple_a)
    ltb = len(tuple_b)
    sumt = ((tuple_a[0] if lta > 0 else 0) + (tuple_b[0] if ltb > 0 else 0),
            (tuple_a[1] if lta > 0 else 0) + (tuple_b[1] if ltb > 1 else 0))
    return sumt
