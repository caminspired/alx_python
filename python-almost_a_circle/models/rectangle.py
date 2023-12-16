""" This module contains the class Base """

class Base:
    """ defines class Base with private attribute __nb_objects """
    __nb_objects = 0
    
    
    def __init__(self, id=None):
        """
        initializes an instance of class Base 
        
        Variables"
        __nb_objects = 0
        
        Args:
        id = None
        """
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
                
class Rectangle(Base):
    """ 
    defines class Rectangle as a subclass of class Base
    
    Attributes:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    """
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes an instance of class Rectangle """
        
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width """
        self.__width = value

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height """
        self.__height = value

    @property
    def x(self):
        """ getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x """
        self.__x = value

    @property
    def y(self):
        """ getter method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y """
        self.__y = value
