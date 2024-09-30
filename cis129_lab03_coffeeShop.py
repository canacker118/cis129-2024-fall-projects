# Prices
coffee_price = 5
muffin_price = 4
tax_rate = 0.06

# Input from the user
print("My Coffee and Muffin Shop")
print()
num_coffees = int(input("Number of coffees bought?: "))
num_muffins = int(input("Number of muffins bought?: "))
print()

# Calculating subtotal
subtotal = (num_coffees * coffee_price) + (num_muffins * muffin_price)

# Calculating item totals
coffee_total = num_coffees * coffee_price
muffin_total = num_muffins * muffin_price

# Calculating tax
tax = subtotal * tax_rate

# Total amount
total = subtotal + tax

# Display the results
print("My Coffee and Muffin Shop Receipt")
print(f"\n{num_coffees} Coffee at ${coffee_price} each: ${coffee_total:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price} each: ${muffin_total:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")

