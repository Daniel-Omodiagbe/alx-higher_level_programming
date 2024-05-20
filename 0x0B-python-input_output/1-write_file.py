#!/usr/bin/python3
"""documentation for write_file module"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
        and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as fs:
        file = fs.write(text)
        return (len(text))
    fs.close
