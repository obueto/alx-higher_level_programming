#!/usr/bin/python3
''' Defines a class named Square '''



class Square:
    ''' class named Square '''

    def __init__(self, size=0, position=(0, 0)):
        ''' Initalises a new square with a size '''
        self.__size = size
        self.position = position

    @property
    def size(self):
        ''' getter method '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' setter method '''

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must >= 0")
        self.__size = value

    @property
    def position(self):
        ''' getter method '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' setter method '''

        if (not isinstance(value, tuple)) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = value

        def area(self):
            ''' Returns the area of a square '''
            return(self.__size * self.__size)

        def my_print(self):
            ''' Prints a square with the character # '''
            if self.__size == 0:
                print("")
            else:
                for x in range(self.__position[1]):
                    print()
                for y in range(self.__size):
                    print("{}{}".format(" "*self.__position[0], "#"*self.__size))
