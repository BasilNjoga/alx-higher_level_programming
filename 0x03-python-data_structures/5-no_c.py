#!/usr/bin/python3

def no_c(my_string):
    new_string = list(my_string)
    for x in range(len(new_string)):
        if new_string[x] == "c" or new_string[x] == "C":
            new_string[x] = " "
    s = ""
    s = s.join(new_string)
    return s

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
