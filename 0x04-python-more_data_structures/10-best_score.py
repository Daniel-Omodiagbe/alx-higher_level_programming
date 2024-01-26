#!/usr/bin/python3


def best_score(a_dictionary):
    """function that returns a key with the biggest integer value"""

    if a_dictionary is not None:
        value = list(a_dictionary.values())
        valu = value[0]
        for key, val in a_dictionary.items():
            if val >= valu:
                valu = val
                name = key
        return name
    else:
        return None
