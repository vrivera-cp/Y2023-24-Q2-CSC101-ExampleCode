"""immutable.py"""

greeting = 'Hello'
greeting = greeting + ', '
greeting = greeting + 'world!'

print('J' + greeting[1:])  # Slice notation, Output: 'Jello, world!'

greeting[0] = 'J'  # TypeError: 'str' object does not support assignment...