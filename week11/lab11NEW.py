print("--- Exercise 1 ---")
customer = {
        "name": "Alice",
        "Name": "Not-Alice",
        "email": "alice@example.com",
        "tier": "gold",
        "ytd_spending": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spending"])


print("--- Exercise 2 ---")
customer['phone'] = "555-5555"
print(customer["phone"])
customer['tier'] = "platinum"
print(customer["tier"])
del customer['Name']
print(customer)


print(customer.get("Name", "Not found"))

print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))

#try:
    #print(customer["email"])
#except KeyError as error:
    #print("KeyError:", error)

print("--- Exercise 4 ---")
for key in customer:
    print(key, ":", customer[key])

for something in customer:
    print(something, customer[something])

print("--- Exercise 5 ---")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.1, "platinum": 0.15}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"tier: {customer['tier']}, discount rate: {discount_rate:.0%}")
print(f"Discount amount: ${purchase * discount_rate:.2f}")
print(f"Final price: ${final_price:.2f}")

print("--- Exercise 6 ---")
customers = [
    {"name": "Bob", "tier": "silver", "ytd_spending": 3200},
    {"name": "Carol", "tier": "gold", "ytd_spending": 8750},
    {"name": "David", "tier": "bronze", "ytd_spending": 450},
]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

print("--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details['stock']} left!")

print("--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")

# Reflection

# 1. I'd use .get() when a key might be missing and a default is fine, like an
# optional phone number or an unknown discount tier. I'd use brackets when the
# key has to exist, like a customer's name, so a missing key shows me there's
# a problem. Rule of thumb: missing is okay -> .get(); missing is a bug -> brackets.

# 2. This is like a SUMIF or pivot table in Excel. Python is better for big
# datasets because it handles way more rows and you can rerun the same
# script on new data instead of redoing it by hand.