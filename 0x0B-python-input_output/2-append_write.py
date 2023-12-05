#!/usr/bin/python3
"""Writes a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
