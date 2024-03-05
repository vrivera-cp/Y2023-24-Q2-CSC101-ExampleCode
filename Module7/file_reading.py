"""file_reading.py"""

if __name__ == '__main__':
    with open('mochi.txt') as f:
        for line in f:
            line = line.strip()  # Remove leading and trailing whitespace
            print(line)