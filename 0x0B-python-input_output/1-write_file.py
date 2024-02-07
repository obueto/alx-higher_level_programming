#!/usr/bin/python3

""" Defines a function that writes a string to a text file """


def write_file(filename="", text=""):
    """ writes string to file and return the number of characters """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
