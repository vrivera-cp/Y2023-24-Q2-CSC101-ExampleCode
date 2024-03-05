"""file_writing.py"""

import random

if __name__ == '__main__':

    numbers = 100
    x = [random.random() * 25 for i in range(numbers)]
    y = [random.random() * 25 for i in range(numbers)]

    with open('numbers.txt', 'w') as f:
        for i in range(numbers):
            z = x[i] + y[i]
            f.write(f'{z:.2f}\n')