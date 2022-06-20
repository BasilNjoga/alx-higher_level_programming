#!/usr/bin/python3

def safe_print_integer(value):
    j = value
    try:
        j = j / 3
        print("{:d}".format(value)) 
        return(True)     
    except:
        return(False)

