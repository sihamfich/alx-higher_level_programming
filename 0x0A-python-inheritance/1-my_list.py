#!/usr/bin/python3
"""Module for class MyList"""


class MyList(list):
    """Implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """Printing a list in sorted ascending order"""
        print(sorted(self))
