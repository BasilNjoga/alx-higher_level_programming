#!/usr/bin/python3
"""This is an algorithm to find the peak in a list """

def find_peak(list_of_integers):
    """ This function finds the peak ina list"""
    start = 2
    middle = 3
    end = 4
    mylist = list_of_integers
    if (mylist == None):
        return (NULL)
    for i in range(1, len(mylist) - 1):
        if ((mylist[i] > mylist[i+1]) & (mylist[i] > mylist[i-1])):
            return mylist[i]

