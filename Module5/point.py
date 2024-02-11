"""point.py"""


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y


if __name__ == '__main__':
    p = Point(3, 4)

    print(p.x)  # Output: 3
    print(p.y)  # Output: 4

    print(p)  # Output: (3, 4)
    print(f"The point is {p}")  # Output: The point is (3, 4)

    a = Point(3, 4)
    b = Point(4, 3)
    c = Point(3, 4)

    print(a == a)  # Output: True
    print(a == b)  # Output: False
    print(a == c)  # Output: True
    print(a == (3, 4))  # Output: False
