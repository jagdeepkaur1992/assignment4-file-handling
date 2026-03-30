# Task 1: Write Sales Records to a File

sales = [1200, 450, 980, 1500, 3000]

# Write each sale on a new line
with open("sales_data.txt", "w") as file:
    for s in sales:
        file.write(str(s) + "\n")

print("Data written to file.\n")

# Reopen and print contents
with open("sales_data.txt", "r") as file:
    print("File Content:")
    print(file.read())


# 🔹 Extra (Optional): Comma-separated format
with open("sales_data_comma.txt", "w") as file:
    file.write(",".join(map(str, sales)))

print("\nComma-separated file created.")