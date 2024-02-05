"""aliasing.py"""

# Two new list objects
a = [1, 2, 3]
b = [1, 2, 3]
a.append(4)
print(a, b)  # Output: [1, 2, 3, 4] [1, 2, 3]

# One list object
a = [1, 2, 3]
b = a
a.append(4)
print(a, b)  # Output: [1, 2, 3, 4] [1, 2, 3, 4]
