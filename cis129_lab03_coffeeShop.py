# Prices
coffee_price = 5
herbalTea_price = 5
muffin_price = 4
scone_price = 3
tax_rate = 0.06

# User Input
print("My Coffee and Muffin Shop")
print()
num_coffees = int(input("Number of coffees bought?: "))
num_muffins = int(input("Number of muffins bought?: "))
num_herbalTea = int(input("Number of herbal teas bought?: "))
num_scone = int(input("Number of scones bought?: "))
print()

# Calculating subtotal
subtotal = (num_coffees * coffee_price) + (num_muffins * muffin_price) + (num_herbalTea * herbalTea_price) + (num_scone * scone_price)

# Calculating item totals
coffee_total = num_coffees * coffee_price
herbalTea_total = num_herbalTea * herbalTea_price
muffin_total = num_muffins * muffin_price
scone_total = num_scone * scone_price

# Calculating tax
tax = subtotal * tax_rate

# Total amount
total = subtotal + tax

# Results
print("My Coffee and Muffin Shop Receipt")
print(f"\n{num_coffees} Coffee at ${coffee_price} each: ${coffee_total:.2f}")
print(f"{num_herbalTea} Herbal Tea at ${herbalTea_price} each: ${herbalTea_total:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price} each: ${muffin_total:.2f}")
print(f"{num_scone} Scones at ${scone_price} each: ${scone_total:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")

