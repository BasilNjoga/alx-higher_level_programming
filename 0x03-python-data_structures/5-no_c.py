#!/usr/bin/python3

def no_c(my_string):
    new_string = list(my_string)
    line = []
    for x in range(len(new_string)):
        if new_string[x] == "c" or new_string[x] == "C":
            line.append(x)
    for y in range(len(line)):
        new_string.remove(line[y])
    s = ""
    s = s.join(new_string)
    return s
