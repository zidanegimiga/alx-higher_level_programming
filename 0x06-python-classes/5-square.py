#!/usr/bin/python3
"""Contains a definition of a class Square."""


class Square:
    """Definition of a class Square."""

    def __init__(self, size=0):
        """Initializes an object of the class Square.
        Ensures that the parameter passed is of type int and is not less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Returns the value of the size attribute
        Setter method sets the value of self.__size to value
        Ensures that the parameter passed is of type int and is not less than 0
        """

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square's area"""

        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character '#'"""

        if self.__size == 0:
            print()
        else:
            for n in range(0, self.__size):
                print('#' * self.__size)
