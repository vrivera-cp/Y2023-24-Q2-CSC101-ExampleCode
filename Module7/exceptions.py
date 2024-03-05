"""exceptions.py"""

if __name__ == '__main__':
    file_path = input('Enter a file name: ')
    numbers = []
    try:
        with open(file_path) as f:
            for line in f:
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print("Could not convert line to a float!")

    except FileNotFoundError:
        print(f"File {file_path} does not exist!")

    try:
        print(numbers[0] + numbers[1])
    except IndexError:
        print("Not enough values!")