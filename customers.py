# Exercise 1: One Customer
customer = {
    "name": "Alice",
    "email": "alice@gmail.com",
    "tier": "gold",
    "ytd_spend": 500
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print (customer)

# Exercise 2: Update and Add
customer["phone"] ="123-456-7890"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)