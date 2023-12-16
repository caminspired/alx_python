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
        
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        
        elif value <= 0:
            raise ValueError("width must be > 0")
        
        self.__width = value

    @property
    def height(self):
        """ getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height """
        
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        
        elif value <= 0:
            raise ValueError("height must be > 0")
        
        self.__height = value

    @property
    def x(self):
        """ getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x """
        
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        
        elif value < 0:
            raise ValueError("x must be >= 0")
        
        self.__x = value

    @property
    def y(self):
        """ getter method for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y """
        
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        
        elif value < 0:
            raise ValueError("y must be >= 0")
        
        self.__y = value

    def area(self):
        """ method for calculation the area of the rectangle """
        
        return self.__width * self.__height
    
    def display(self):
        """ displays the rectangle by printing in stdout the Rectangle instance with the character # taking x and y into account """
        
        for y in range(self.__y):
            print()
            
        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
            
    def __str__(self):
        """ string representation of the Rectangle """
        
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)


    def update(self, *args, **kwargs):
        """ assigns no-keyword and keyword arguments to each attribute """
        
        attributes = ["id", "width", "height", "x", "y"]
        
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
            
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
        
class Square(Rectangle):
    """ defines a class Square as a subclass of class Rectangle """
    
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes an instance of class Square """
        
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """ string representation of the square """
        
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        """ getter method for size """
        
        return self.width

    @size.setter
    def size(self, value):
        """ setter method for size """
        
        self.width = value
        self.height = value

    def __str__(self):
        """ string representation of the square """
        
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
