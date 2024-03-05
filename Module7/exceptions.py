"""exceptions.py"""

if __name__ == '__main__':
    try:
        result = 10 / 0

        my_list = [0, 1, 2]
        print(my_list[4])

        num = int(input("Enter an int: "))
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except (IndexError, ValueError):
        print("Index out of range!")
    except:
        print("An exception occurred!")
    else:
        print("No exceptions occurred!")
    finally:
        print("End of program.")
