#!/usr/bin/python3
"""the rectangle module"""
from models.base import Base


class Rectangle(Base):
    """this class inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """attributes instantiation"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def display(self):
        """displays the rectangle with "#'s" """
        print("\n"*self.x, end="")
        for row2 in range(self.height):
            print(" "*self.x + "#"*self.width)

    def __str__(self):
        """string representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, 
                                                        self.x, self.y, self.width, self.height)
    def update(self, *args, **kwargs):
        """updates for attributes of rectangle"""
        attrs = ["id", "width", "height", "x", "y"]

        for position, value in enumerate(args):
            if position > (len(attrs) - 1 ):
                break
            setattr(self, attrs[position], value)

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dict representation of rectangle"""
        new_dict = {}
        attrs = ["id", "width", "height", "x", "y"]

        for att in attrs:
            new_dict[att] = getattr(self, att)

        return new_dict

    def area(self):
        """area of the rectangle"""

        return self.width * self.height

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """getter for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
