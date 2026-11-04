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
print(f"Discounted price: ${discount_rate * 100}%")
print(f"Final price: ${final_price:.2f}")
