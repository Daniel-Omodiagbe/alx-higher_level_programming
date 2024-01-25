#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """function that replaces or adds key/value in a dictionary"""

    for keyy, val in a_dictionary.items():
        if keyy == key:
            a_dictionary[key] = value
    if key not in a_dictionary.keys():
        a_dictionary[key] = value
    return a_dictionary
