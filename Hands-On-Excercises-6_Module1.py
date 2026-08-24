customers = [
{"id": 101, "name": "Acme", "active": True, "revenue": 2500000},
{"id": 102, "name": "Global", "active": False, "revenue": 5000000},
{"id": 103, "name": "ABC", "active": True, "revenue": 750000}
]

for customer in customers:
    if customer["active"] == True and customer["revenue"] > 1000000:
        print(customer)
