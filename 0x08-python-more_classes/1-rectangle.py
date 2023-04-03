#!/usr/bin/python3
# File - 1-rectangle.py
# Arth: Mahmud

"""Defines a rectangle"""

class Rectangle:
    """Represents a rectangle with some instances"""
    def __init__(self, width=0, height=0):
        """New rectangle initialisation

        Arguments
            width : Integer width given to the new rectangle
            height : Integer height given to the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Rectangle width value retrival"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the rectangle width value"""
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Rectangle height value retrival"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the rectangle height"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

