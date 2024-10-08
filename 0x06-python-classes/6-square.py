#!/usr/bin/python3
"""Square class definition"""


class Square():
    """ representation of a square class"""

    def __init__(self, size=0, position=(0, 0)):
        """ initializsa5tion of new square, default position value of 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """set positon property"""
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints square area with # character"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for item in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
