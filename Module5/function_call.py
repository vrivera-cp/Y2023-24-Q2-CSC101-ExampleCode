"""function_call.py"""


class Cat:
    """Represent a cat."""


def rename(x: Cat, y: str) -> None:
    """(Re-)assign the cat's name."""
    x.name = y


if __name__ == '__main__':
    cat = Cat()
    cat.name = "mochi"
    print(cat.name)
    rename(cat, "momo")
    print(cat.name)
