#!/usr/bin/python3
def safe_print_integer_err(value):
    """prints an integer"""
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        print(f"Exception: {err}")
    return False
