#!/usr/bin/python3
""" this module contains subclass Rectange that inherits from class BaseGeometry """

from 5-base_geometry import class BaseGeometry

class Rectangley:
    """ defines the subclass Rectangle """

    def __init__(self, width, height):
        """ 
        defines an instance of the class Rectange
        
        Attributes:
        
        Width: must be private and a positive integer
        height: must be private an a positive integer
        
        check with integer_validator
        """
        
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
