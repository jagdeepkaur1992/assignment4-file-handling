# -------------------------------
# Task 7: Mini Project - Discount Report
# -------------------------------

print("\n--- Task 7: Discount Report ---")

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

# Ask user for discount
discount_percent = float(input("Enter discount percentage: "))

discounted_prices = []

# Write to file
with open("discount_report.txt", "w") as file:
    file.write("Product | Original Price | Discounted Price\n")
    file.write("-" * 45 + "\n")

    for product, price in prices.items():
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount

        discounted_prices.append(final_price)

        file.write(f"{product} | {price} | {int(final_price)}\n")

    # Extra: Summary
    total_items = len(prices)
    avg_price = sum(discounted_prices) / total_items

    file.write("\n--- Summary ---\n")
    file.write(f"Total Items: {total_items}\n")
    file.write(f"Average Discounted Price: {int(avg_price)}\n")

print("\nDiscount report generated successfully.\n")

# Read and print file
with open("discount_report.txt", "r") as file:
    print("Discount Report:\n")
    print(file.read())