#!/usr/bin/python3


def no_c(my_string):
    """function that removes all characters c and C from a string"""
    res = []
    for i in my_string:
        if i not in 'cC':
            res.append(i)
    return ''.join(res)
