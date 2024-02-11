"""rectangle.py"""
from point import Point


class Rectangle:
    """Represent a rectangle with top-left and bottom-right coordinates."""

    def __init__(self, top_left: Point, bottom_right: Point) -> None:
        self.top_left = top_left
        self.bottom_right = bottom_right
