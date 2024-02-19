"""filter_pattern.py"""


def filter_loop(ls: list[int]) -> list[int]:
    """A filter function template.

    The only part that will change between different filters
    is the filtering criteria.

    The given template filters out zero and negative values.
    """
    out = []
    for x in ls:
        if x > 0:  # The filtering criteria
            out.append(x)
    return out


def filter_comp(ls: list[int]) -> list[int]:
    """The above filter template as a list comprehension."""
    return [x for x in ls if x > 0]
