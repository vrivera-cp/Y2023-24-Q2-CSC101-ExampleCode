"""list_arguments.py"""


def mochify(strings: list[str]) -> None:
    """Mochify the list."""
    strings.insert(0, 'mochi')
    strings.append('mochi')


if __name__ == '__main__':
    letters = ['a', 'b', 'c']
    mochify(letters)
    print(letters)  # Output: ['mochi', 'a', 'b', 'c', 'mochi']
