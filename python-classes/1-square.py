"""
This module defines a Square class.

The Square class represents a square geometric shape and has a private
instance attribute for the size.

Example:
    square = Square(5)
    print(square.get_area())  # Output: 25
"""

class Square:
    """This class defines a Square.

    Attributes:
        __size (int): Private instance attribute representing the size of the square.
    """

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        
        """The if statement checks to see if the if the value entered for size is an
        integer and whether it is less than 0 and raises the following errors respectively.

        Raises:
            TypeError: "size must be an integer"
            ValueError: "size must be >= 0"
            """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
      
