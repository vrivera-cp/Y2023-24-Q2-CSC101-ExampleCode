"""file_writing.py"""

from random import random

if __name__ == '__main__':
    n = 10
    x = [random() for i in range(n)]
    y = [random() for i in range(n)]

    with open('numbers.txt', 'w') as f:
        for i in range(n):
            z = x[i] + y[i]
            f.write(f'{z:.2f}\n')