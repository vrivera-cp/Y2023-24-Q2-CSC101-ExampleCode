"""control.py"""


def incomplete_function():
    pass  # Needed to prevent a syntax error


x = 0
while True:  # Indefinitely repeat
    x = x + 1
    if x > 4:
        break
    elif x < 4:
        continue
    print(x)
