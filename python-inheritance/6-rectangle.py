#!/usr/bin/python3
""" this module contains subclass Rectange that inherits from class BaseGeometry """

class BaseGeometry:
    """ defines the class BaseGeometry """

    def area(self):
        """
        Calculate the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """ validates the given value is a positive integer """
        
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


    class Rectangle:
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
