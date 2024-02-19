"""map_pattern.py"""


def map_loop(ls: list[int]) -> list[float]:
    """A mapping function template.

    The only parts that will change between different maps
    will be the list types (which may be the same or different)
    and the transformation function.

    The given template maps integers to corresponding float values.
    """
    out = []
    for x in ls:
        y = x * 1.0  # The mapping function
        out.append(y)
    return out


def map_comp(ls: list[int]) -> list[float]:
    """The above map template as a list comprehension."""
    return [x * 1.0 for x in ls]
