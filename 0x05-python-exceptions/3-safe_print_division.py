#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
        return (result)
    except ZeroDivisionError:
        return (None)
    finally:
        try:
            result = a / b
            return(result)
        except:
            result = None
        print("Inside result: {}".format(result))
        #return(result)

