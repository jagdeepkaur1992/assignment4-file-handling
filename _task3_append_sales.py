# Task 3: Append New Sales

new_sales = [5000, 2500, 1700]

# Append data to file
with open("sales_data.txt", "a") as file:
    for s in new_sales:
        file.write(str(s) + "\n")

print("New sales appended.\n")

# Reopen and print updated file
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

print("Updated File Content:")
for line in lines:
    print(line.strip())

# 🔹 Extra: Total number of lines
print("\nTotal number of lines:", len(lines))