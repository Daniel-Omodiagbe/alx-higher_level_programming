#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """function that prints the first x
    elements of a list and only integers"""

    count = 0
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            count += 1
        print()
    except (IndexError, TypeError, ValueError):
        print()
    return count
