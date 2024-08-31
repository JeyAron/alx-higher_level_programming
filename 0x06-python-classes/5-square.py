#!/usr/bin/python3
""" Square class defintion"""


class Square:
    """ representation of a square class"""

    def __init__(self, size=0):
        """ initialization of new square
        """
        self.__size = size

        """ Get the square size"""
    @property
    def size(self):
        """get size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ print square with # character """
        if self.__size == 0:
            print()
        for item in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
