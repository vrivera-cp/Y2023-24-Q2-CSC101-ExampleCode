"""list_methods.py"""

a = [1, 2, 3]
b = [4, 5, 6]

a.add(4)
print(a)  # Output: [1, 2, 3, 4]

del b[0]
b.pop(1)
print(b)  # Output: [5]