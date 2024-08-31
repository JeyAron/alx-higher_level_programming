#!/usr/bin/python3
""" Square class definiton"""


class Square:
    """ representation of a square class"""

    def __init__(self, size=0):
        """ initialization of our new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
