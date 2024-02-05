"""string_methods.py"""

name = input("What's your name? ")

print(name.upper())
print(name.lower())
print(name.capitalize())

print(name.startswith('mo'))
print(name.replace('i', 'a'))
print(name.isalpha())

print(name.split('🐈'))