"""sort.py"""

from swap import swap_in as swap


def selection_sort(ls: list[int]) -> None:
    """Perform in-place selection sort."""
    for i in range(len(ls)):
        i_min = i
        for j in range(i, len(ls)):
            if ls[j] < ls[i_min]:
                i_min = j
        swap(ls, i, i_min)


def insertion_sort(ls: list[int]) -> None:
    """Perform in-place insertion sort."""
    for i in range(len(ls)):
        for j in range(i, 0, -1):
            if ls[j] < ls[j - 1]:
                swap(ls, j, j - 1)
            else:
                break
