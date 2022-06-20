#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    j = 0
    y = []
    if x == 0:
        return(0)
    else:
        try:
            y.append(my_list[x-1])
            y.clear()
            while x > 0:
                print("{}".format(my_list[j]),end="")
                j = j + 1
                x = x - 1
            print("\n",end="")
            return(j)
        except:
            for i in my_list:
                print("{}".format(i),end="")
                j = j + 1
            print("\n",end="")
            return(j)

