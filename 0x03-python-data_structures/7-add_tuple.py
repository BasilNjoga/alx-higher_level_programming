#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)
    if len1 == 1 and len2 == 2:
        tuple_c = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
    elif len1 == 0 and len2 == 2:
        tuple_c = (0 + tuple_b[0], 0 + tuple_b[1])
    elif len2 == 1 and len1 == 2:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    elif len2 == 0 and len1 == 2:
        tuple_c = (tuple_a[0] + 0, tuple_a[1] + 0)
    elif len1 == 1 and len2 == 1:
        tuple_c = (tuple_a[0] + tuple_b[0], 0 + 0)
    elif len1 == 0 and len2 == 0:
        tuple_c = (0 + 0, 0 + 0)
    else:
        tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return tuple_c

tuple_a = ()
tuple_b = ()
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)