#!/usr/bin/python3
""" This is a module that inherist a list """
class list:

    def __init__(self):
        self.numbers = []

    def append(self, num):
        self.numbers.append(num)

    def __str__(self):
        return str(self.numbers)


class MyList(list):
    """This is a list that inherits from another """
    
    def print_sorted(self):
        self.newnumbers = self.numbers[:]
        for j in range(len(self.newnumbers)):
            for i in range(len(self.newnumbers) - 1):
                if self.newnumbers[i] > self.newnumbers[i+1]:
                    newlist = self.newnumbers[i]
                    self.newnumbers[i] = self.newnumbers[i+1]
                    self.newnumbers[i+1] = newlist
        print(self.newnumbers)
