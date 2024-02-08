#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints an integer"""
    try:
        print("{:d}".format(value))
        return True
    except TypeError as err:
        print(f"Exception: {err}")
    return False
