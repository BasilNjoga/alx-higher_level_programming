#!/usr/bin/python3
"""This is an algorithm to find the peak in a list """

def fin_peak(list_of_integers):
    """ This function finds the peak ina list"""
    mylist = list_of_integers
    if (mylist == NULL):
        return (NULL)
    for i in range(len(mylist)):
        if ((mylist[i] > mylist[i+1]) && (mylist[i] > mylist[i-1])):
            return mylist[i]

