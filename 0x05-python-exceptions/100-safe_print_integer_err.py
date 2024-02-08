#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints an integer"""
    try:
        if value is isinstance(value, int):
            print("{}".format(value))
            return True
    except TypeError as err:
        print(err)
        return False
