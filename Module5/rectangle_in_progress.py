"""rectangle_in_progress.py"""
from point_in_progress import Point


class Rectangle:
    """Represent a rectangle."""


if __name__ == '__main__':
    r = Rectangle()
    r.top_left = Point()
    r.bottom_right = Point()
    r.top_left.x = 4
    r.top_left.y = 10
    r.bottom_right.x = 10
    r.bottom_right.y = 4
