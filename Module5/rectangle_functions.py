"""rectangle_functions.py"""
from rectangle import Rectangle


def get_width(rectangle: Rectangle) -> float:
    """Return the rectangle's width, assuming it is properly axis aligned."""
    return rectangle.bottom_right.x - rectangle.top_left.x


def get_height(rectangle: Rectangle) -> float:
    """Return the rectangle's height, assuming it is properly axis aligned."""
    return rectangle.top_left.y - rectangle.bottom_right.y


def get_area(rectangle: Rectangle) -> float:
    """Return the rectangle's area, assuming it is properly axis aligned."""
    return get_width(rectangle) * get_height(rectangle)


def get_largest_rectangle(rectangles: list[Rectangle]) -> Rectangle | None:
    """Return the largest, properly axis-aligned, rectangle."""
    largest_rectangle = None

    for rectangle in rectangles:
        pass  # Unimplemented

    return largest_rectangle
