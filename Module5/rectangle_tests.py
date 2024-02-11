"""rectangle_tests.py"""
import unittest

from point import Point
from rectangle import Rectangle

from rectangle_functions import get_width, get_height, get_area, get_largest_rectangle


class RectangleTests(unittest.TestCase):

    def test_get_width(self):
        top_left = Point(4, 10)
        bottom_right = Point(10, 4)

        rectangle = Rectangle(top_left, bottom_right)

        self.assertEqual(0, get_width(rectangle))  # Incomplete

    def test_get_height(self):
        pass  # Incomplete

    def test_get_area(self):
        pass  # Incomplete

    def test_largest(self):
        rectangles = []

        # Append to rectangle instances to the list here

        self.assertEqual(0, get_largest_rectangle(rectangles))  # Incomplete


if __name__ == '__main__':
    unittest.main()
