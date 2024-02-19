"""fold_pattern.py"""


def fold(ls: list[int]) -> int:
    """A fold function template.

    The only parts that will change between different folds
    are the accumulator initial value and combining function.

    The given template filters out zero and negative values.
    """
    a = 0  # Accumulator
    for x in ls:
        a = a + x  # Combining function
    return a
