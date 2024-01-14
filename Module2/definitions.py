"""definitions.py
An example showing different function definitions with example calls.
"""


# A non-fruitful function without parameters
def greet() -> None:
    """Print a generic greeting."""
    print('Hello!')


# A non-fruitful function with a parameter
def greet_by_name(name: str) -> None:
    """Print a greeting to the given person."""
    print(f'Hello {name}!')


# A fruitful function without parameters
def meow() -> str:
    """Return the string 'Meow'."""
    return 'Meow'


# A fruitful function with a parameter
def get_cat_meow(cat: str) -> str:
    """Return a string containing the given cat's name followed by 'Meow'."""
    return cat + ': ' + meow()


# A fruitful function with one parameter
def calculate_grounds(water: float) -> float:
    """Return coffee in tbsp based on the given water in oz."""
    grounds = water * (5 / 36)
    return grounds


# A fruitful function with parameters
def calculate_center(left: float, right: float) -> float:
    """Return the position at the center of two positions along an axis."""
    middle = (left + right) / 2
    return middle


# A main guard
if __name__ == '__main__':
    greet()
    print(greet())

    greet_by_name('mochi')
    print(greet_by_name('harvest'))

    cat = 'pearl'
    greet_by_name(cat)

    meow()
    print(meow())

    statement = get_cat_meow(cat)
    print(statement)

    left = 3.0
    right = 6.0
    print(calculate_center(left, right))
