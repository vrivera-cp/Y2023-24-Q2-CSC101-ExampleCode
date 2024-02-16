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

        self.assertEqual(6, get_width(rectangle))  # Incomplete

    def test_get_height(self):
        self.assertEqual(9, get_height(Rectangle(Point(1, 10), Point(10, 1))))


    def test_get_area(self):
        top_left = Point(0, 2)
        bottom_right = Point(2, 0)

        rectangle = Rectangle(top_left, bottom_right)

        self.assertEqual(1, get_area(rectangle))

    def test_largest(self):
        rectangles = []

        rectangles.append(Rectangle(Point(0, 1), Point(1, 0)))
        rectangles.append(Rectangle(Point(0, 2), Point(2, 0)))

        self.assertEqual(Rectangle(Point(0, 2), Point(2, 0)), get_largest_rectangle(rectangles))  # Incomplete


if __name__ == '__main__':
    unittest.main()
