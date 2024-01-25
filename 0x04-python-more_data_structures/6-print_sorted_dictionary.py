#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys"""

    new_dict = sorted(a_dictionary.items())
    for key, val in new_dict:
        print("{}: {}".format(key, val))
