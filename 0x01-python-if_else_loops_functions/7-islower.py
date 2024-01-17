#!/usr/bin/python3
def islower(c):
    """checks for lower case characters"""
    if c >= chr(97) and c <= chr(123):
        return True
    else:
        return False
