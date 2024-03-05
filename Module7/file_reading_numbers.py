"""file_reading_numbers.py"""

if __name__ == '__main__':
    numbers = []

    with open('numbers.txt') as f:
        for line in f:
            line = line.strip()  # Remove leading and trailing whitespace
            numbers.append(float(line))
    print(numbers)

    total = 0.0
    for number in numbers:
        total += number
    print(total)