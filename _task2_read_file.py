# Task 2: Read File in Different Ways

# 1. Read entire file using .read()
with open("sales_data.txt", "r") as file:
    data = file.read()
    print("Using read():")
    print(data)

# 2. Read first line using .readline()
with open("sales_data.txt", "r") as file:
    first_line = file.readline().strip()
    print("\nUsing readline():")
    print(first_line)

# 3. Read all lines using .readlines() and convert to integers
with open("sales_data.txt", "r") as file:
    lines = file.readlines()
    numbers = [int(line.strip()) for line in lines]

    print("\nUsing readlines():")
    print(numbers)