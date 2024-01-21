"""logical.py"""

x = True
y = False

print(not x)    # not True,       Output: False
print(not y)    # not False,      Output: True
print(x and y)  # True and False, Output: False
print(x or y)# True or False,  Output: False

print(True or False and not False)  # Output: True
