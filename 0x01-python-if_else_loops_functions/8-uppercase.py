#!/usr/bin/python3

def uppercase(str):
    for i in str:
        n = ord(i)
        if n > 90:
            n = n - 32
        else:
            n = n
        print("{}".format(chr(n)),end='')
    print("\n")
