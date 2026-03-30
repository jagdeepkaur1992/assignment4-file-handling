# Task 6: Read File Safely (Without Exceptions)

import os

# Ask user for filename
filename = input("Enter filename to open: ")

# Check if file exists
if os.path.exists(filename):
    with open(filename, "r") as file:
        print("\nFile Content:")
        print(file.read())
else:
    print("File not found. Please check the filename.")
    