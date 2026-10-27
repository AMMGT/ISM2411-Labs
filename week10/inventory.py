# Reflection
# 1. I was surprised that Python lists are both ordered and mutable: I can
#    access items by position and change the collection after creating it.
#    Slices are also useful because they make a new list from selected items
#    without needing to loop over them manually.
# 2. In a business-class sales exercise, a list could hold each day's sales.
#    A short program could filter days above a target and calculate their
#    count and average, instead of selecting and calculating those values by
#    hand in a spreadsheet.

# --- Exercise 1 ---
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# --- Exercise 2 ---
middle_index = len(inventory) // 2
print(inventory[0])
print(inventory[-1])
print(inventory[middle_index])

# --- Exercise 3 ---
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# --- Exercise 4 ---
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# --- Exercise 5 ---
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because their values cannot be changed accidentally.")
print(coords)

# --- Exercise 6 ---
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

# --- Exercise 7 ---
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.90, 2))
print(prices)
print(discounted)

# --- Exercise 8 ---
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
high_sales_average = sum(high_sales) / len(high_sales)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Avg: {high_sales_average:.2f}")
