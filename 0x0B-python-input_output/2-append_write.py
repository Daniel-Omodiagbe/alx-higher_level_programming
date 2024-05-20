#!/usr/bin/python3
"""documentation for append_write module"""


def append_write(filename="", text=""):
    """ function that appends a string at the end of a tex
     file (UTF8) and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as fs:
        file = fs.write(text)
        return (len(text))
    fs.close
