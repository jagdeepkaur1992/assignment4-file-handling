# Task 4: Generate Summary Report from File

# Read data from file
with open("sales_data.txt", "r") as file:
    lines = file.readlines()

# Convert to integers (remove newline)
sales = [int(line.strip()) for line in lines]

# Calculate values
total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sale = total_sales / len(sales)

# Print results
print("Total Sales:", total_sales)
print("Highest Sale:", highest_sale)
print("Lowest Sale:", lowest_sale)
print("Average Sale:", average_sale)
