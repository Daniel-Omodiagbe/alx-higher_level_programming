#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    function that replaces an element in a list at a specific position
    without modifying the original list
    """

    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    modified_list = list(my_list)
    modified_list[idx] = element
    return modified_list
