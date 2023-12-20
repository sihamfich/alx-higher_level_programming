#!/usr/bin/python3
"""A module for square"""


class Square:
    """Define square"""

    def __init__(self, size=0):
        """Constractor
        Args:
            size (int): The size of the square.
        Raise:
            TypeError: If size is not an integer
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
