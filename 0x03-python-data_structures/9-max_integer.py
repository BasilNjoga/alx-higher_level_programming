#!/usr/bin/python3

def max_integer(my_list=[]):
    for x in range(len(my_list)):
        for y in range(len(my_list) - 1):
            if my_list[y] < my_list[y+1]:
                my_list[y+1] = my_list[y]
                my_list[y] = my_list[y+1]                
            print(my_list)
    return my_list

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
print(max_integer(my_list))