# Task 5: Create Product Info File (User Input)

products = []

# Take input from user
for i in range(3):
    name = input(f"Enter product {i+1} name: ")
    price = input(f"Enter product {i+1} price: ")
    products.append((name, price))

# Write to file
with open("products.txt", "w") as file:
    for name, price in products:
        file.write(f"{name} | {price}\n")

print("\nProducts saved to file.\n")

# Read and print formatted output
with open("products.txt", "r") as file:
    print("Product List:")
    for line in file:
        name, price = line.strip().split(" | ")
        print(f"Product: {name}, Price: ₹{price}")
        