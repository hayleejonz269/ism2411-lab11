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

# Exercise 3: Safe Lookup
print(customer.get("email", "no email on file"))
try: 
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")

# exercise 4 Iterate
for key, value in customer.items():
    print(f"{key}: {value}")
# Without .items(), only the keys are printed
for key in customer:
    print(key)
    