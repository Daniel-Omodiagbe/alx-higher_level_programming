#!/usr/bin/python3
def islower(c):
    """checks for upper case characters"""
    if c >= chr(65) and c <= chr(90):
        return True
    else:
        return False
