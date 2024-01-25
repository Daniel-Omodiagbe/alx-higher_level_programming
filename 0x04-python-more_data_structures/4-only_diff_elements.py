#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """function that returns a set of all elements present in only one set"""

    for i in set_1:
        if i not in set_2:
            set_2.add(i)
    return set_2
