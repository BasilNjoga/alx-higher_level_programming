#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    x = 0
    while x < max(len(my_list_1), len(my_list_2)):
        try:
            z = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            z = 0
            pass
        except TypeError:
            print("wrong type")
            z = 0
            pass
        except IndexError:
            print("out of range")
            z = 0
            pass
        finally:
            print("complete")
        new_list.append(z)
        x = x + 1
    return new_list


my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)