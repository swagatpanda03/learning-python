#Dictionary
#used to store key and value pairs

customer = {
    "name": "Swagat Panda",
    "age": 21,
    "is_verified": True
    }

print(customer["name"])

print(customer.get("name"))

print(customer.get("Birthdate", "Jan 1 2000"))

customer["birthdate"] = "29-12-2000"

print(customer)
