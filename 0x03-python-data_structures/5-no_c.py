#!/usr/bin/python3


def no_c(my_string):
    """function that removes all characters c and C from a string"""
    for i in my_string:
        if i != 'c' and i != 'C':
            print("{}".format(i), end="")
