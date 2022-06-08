#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = (sorted(a_dictionary))
    for x in new_list:
        print("{}: {}".format(x, a_dictionary[x]))
