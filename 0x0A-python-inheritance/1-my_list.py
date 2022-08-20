#!/usr/bin/python3
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
        for j in range(len(self.numbers)):
            for i in range(len(self.numbers) - 1):
                if self.numbers[i] > self.numbers[i+1]:
                    newlist = self.numbers[i]
                    self.numbers[i] = self.numbers[i+1]
                    self.numbers[i+1] = newlist
        print(self.numbers)
