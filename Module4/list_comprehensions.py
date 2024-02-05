"""list_comprehensions.py"""
import random

# List Creation
items = [i for i in range(100)]  # [0, 1, 2, 3, ..., 99]
random_items = [random.randint(0, 10) for i in range(100)]

# Mapping
print([number ** 2 for number in items])  # Output: [0, 1, 4, 9, ..., 9801]
print([number ** 2 for number in random_items])

# Filtering
print([x for x in items if x % 2 == 1])  # Output: [1, 3, 5, ..., 99]
print([x for x in random_items if x % 2 == 1])