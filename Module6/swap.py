"""swap.py"""


def swap_in(ls: list[int], i: int, j: int) -> None:
    """Swap the values at i and j swapped."""
    temporary = ls[i]
    ls[i] = ls[j]
    ls[j] = temporary


def swap_out(ls: list[int], i: int, j: int) -> list[int]:
    """Construct a copied list with the values at i and j swapped."""
    swapped = []
    for k in range(len(ls)):
        if k == i:
            swapped.append(ls[j])
        elif k == j:
            swapped.append(ls[i])
        else:
            swapped.append(ls[k])
    return swapped
