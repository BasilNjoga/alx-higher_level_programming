#!/usr/bin/python3

def safe_print_division(a, b):
    val = 0
    if a > 0 and b > 0:
        val = a / b
    else:
        val = None
    try:
        result = a / b
        return (result)
    except ZeroDivisionError:
        return (None)
    finally:
        print("Inside result: {}".format(val))
