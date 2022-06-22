#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    j = 0
    z = 0
    y = []
    while x > 0:
        try:
            k = my_list[j] / 3
            y.append(my_list[j])
            y.clear
            print("{:d}".format(my_list[j]), end="")
            z = z + 1
        except TypeError:
            pass
        j = j + 1
        x = x - 1
    print("\n", end="")
    return(z)
