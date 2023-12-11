#!/usr/bin/python3
"""Module for testing Square"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Tests the square class"""

    def test_id(self):
        """ Tests the id of the rectangle"""

        Base._Base__nb_objects = 0
        s1 = Square(10, 2)
        s2 = Square(1, 1)
        s3 = Square(10, 0, 0, 12)

        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 12)

    def test_size(self):
        """ Test correct size being set"""

        s1 = Square(10, 2)
        s2 = Square(666, 333)

        self.assertEqual(s1.size, 10)
        self.assertEqual(s2.size, 666)

    def test_square_no_arguments(self):
        """ Test when no arguements passed"""

        with self.assertRaises(TypeError):
            s1 = Square()

    def test_with_size_and_x(self):
        """ Test when size and x are passed"""

        s1 = Square(10, 3)

        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 3)

    def test_with_size_x_and_y(self):
        """ Test when size, x and y are passed"""

        s1 = Square(10, 3, 2)

        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 2)

    def test_square_with_negative_x(self):
        """ Test when x is passed a negative number"""

        with self.assertRaises(ValueError) as err:
            s1 = Square(1, -2)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_square_with_negative_y(self):
        """ Test when y is passed a negative number"""

        with self.assertRaises(ValueError) as err:
            s1 = Square(1, 2, -3)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_with_all_arguments(self):
        """ Test when size, x, y and id are passed"""

        s1 = Square(10, 3, 2, 50)

        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 50)

    def test_square_if_area_works(self):
        """ Test is area works in Square"""

        s1 = Square(4, 4, 2, 0)

        self.assertEqual(s1.area(), 16)

    def test_square_setter_getter_one(self):
        """ Test when size is negative"""

        with self.assertRaises(ValueError) as err:
            s1 = Square(-5)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_square_setter_getter_two(self):
        """ Test when size is 0"""

        with self.assertRaises(ValueError) as err:
            s1 = Square(0)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_list_size(self):
        """ Test when size is passed a list"""

        with self.assertRaises(TypeError) as err:
            s1 = Square([5], 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_dict_size(self):
        """ Test when size is passed a dict"""

        with self.assertRaises(TypeError) as err:
            s1 = Square({"size": 5}, 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_float_size(self):
        """ Test when size is passed a float"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(5.5, 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_tuple_size(self):
        """ Test when size is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            s1 = Square((3, 4), 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_square_string_size(self):
        """ Test when size is passed a string"""

        with self.assertRaises(TypeError) as err:
            s1 = Square("Penguin", 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_square_list_x(self):
        """ Test when x is passed a list"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(5, [4], 3, 2)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_square_dict_x(self):
        """ Test when x is passed a dict"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(6, {"x": 5}, 3, 2)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_square_float_x(self):
        """ Test when x is passed a float"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(5, 4.5, 3, 2)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_square_tuple_x(self):
        """ Test when x is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(3, (4, 5), 3, 2)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_square_string_x(self):
        """ Test when x is passed a string"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(5, "Penguin", 4, 3)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_square_list_y(self):
        """ Test when y is passed a list"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(5, 4, [3], 2)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_square_dict_y(self):
        """ Test when y is passed a dict"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(4, 3, {"y": 5}, 2)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_square_float_y(self):
        """ Test when y is passed a float"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(5, 4, 3.5, 2)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_sqaure_tuple_y(self):
        """ Test when y is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(3, 4, (3, 60), 2)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_square_string_y(self):
        """ Test when y is passed a string"""

        with self.assertRaises(TypeError) as err:
            s1 = Square(5, 4, "Penguin", 3)
        self.assertEqual(str(err.exception), "y must be an integer")

