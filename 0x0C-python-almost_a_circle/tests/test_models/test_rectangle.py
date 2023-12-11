#!/usr/bin/python3
"""Module for testing the Rectangle class"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Runs tests on the rectangle class"""

    def test_negative_width(self):
        """Test when width is negative"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(-5, 4, 3, 2)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_zero_width(self):
        """ Test when width is zero"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(0, 50, 2, 3)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_negative_height(self):
        """ Test when height is negative"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(2, -5, 4, 3)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_zero_height(self):
        """ Test when height is zero"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(2, 0, 3, 4)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_negative_x(self):
        """ Test when x is negative"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(1, 2, -3, 4)
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_negative_y(self):
        """ Test when y is negative"""

        with self.assertRaises(ValueError) as err:
            r1 = Rectangle(1, 2, 3, -4)
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_all_args(self):
        """ Test with all argument fields passed"""

        r1 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_list_width(self):
        """ Test when width is passed a list"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle([5], 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_dict_width(self):
        """ Test when width is passed a dict"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle({"width": 5}, 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_float_width(self):
        """ Test when width is passed a float"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5.5, 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_tuple_width(self):
        """ Test when width is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle((3, 4), 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_string_width(self):
        """ Test when width is passed a string"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle("Penguin", 4, 3, 2, 1)
        self.assertEqual(str(err.exception), "width must be an integer")

    def test_list_height(self):
        """ Test when height is passed a list"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, [4], 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_dict_height(self):
        """ Test when height is passed a dict"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, {"height": 5}, 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_float_height(self):
        """ Test when height is passed a float"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4.5, 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_tuple_height(self):
        """ Test when height is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(3, (4, 5), 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_string_height(self):
        """ Test when height is passed a string"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, "Penguin", 3, 2, 1)
        self.assertEqual(str(err.exception), "height must be an integer")

    def test_list_x(self):
        """ Test when x is passed a list"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, [3], 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_dict_x(self):
        """ Test when x is passed a dict"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, 3, {"x": 5}, 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_float_x(self):
        """ Test when x is passed a float"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, 3.5, 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_tuple_x(self):
        """ Test when x is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(3, 4, (3, 2), 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_string_x(self):
        """ Test when x is passed a string"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, 3, "Penguin", 2, 1)
        self.assertEqual(str(err.exception), "x must be an integer")

    def test_list_y(self):
        """ Test when y is passed a list"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, 3, [2], 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_dict_y(self):
        """ Test when y is passed a dict"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, 3, 2, {"y": 5}, 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_float_y(self):
        """ Test when y is passed a float"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(5, 4, 3, 2.5, 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_tuple_y(self):
        """ Test when y is passed a tuple"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(3, 4, 3, (1, 2), 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_string_y(self):
        """ Test when y is passed a string"""

        with self.assertRaises(TypeError) as err:
            r1 = Rectangle(4, 3, 2, "Penguin", 1)
        self.assertEqual(str(err.exception), "y must be an integer")

    def test_area(self):
        """ Test for correct output for area"""

        r1 = Rectangle(3, 3, 0, 0, 10)
        r2 = Rectangle(4, 4)
        r3 = Rectangle(2, 2, 3)
        r4 = Rectangle(2, 1, 4, 3)

        self.assertEqual(r1.area(), 9)
        self.assertEqual(r2.area(), 16)
        self.assertEqual(r3.area(), 4)
        self.assertEqual(r4.area(), 2)

    def test_display_number_zero(self):
        """ Test if display of rectangle is correct"""

        display = "##\n##\n##\n"
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        r1 = Rectangle(2, 3)

        r1.display()
        self.assertEqual(capturedOutput.getvalue(), display)

        sys.stdout = sys.__stdout__ 
