#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """function that returns a set of all elements present in only one set"""

    new_list = []
    for i in set_1:
        new_list.append(i)
    for i in set_2:
        new_list.append(i)
    return set(new_list)
