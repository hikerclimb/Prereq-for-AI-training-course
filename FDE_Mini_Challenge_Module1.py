orders = [
{"id": 1001, "customer": "ABC", "amount": 1200, "status": "completed"},
{"id": 1002, "customer": "XYZ", "amount": 450, "status": "failed"},
{"id": 1003, "customer": "Acme", "amount": 2500, "status": "completed"}
]

total_amount = 0
for order in orders:
    if order["status"] == 'completed' and order["amount"] > 1000:
        print(order["customer"])
        total_amount += order["amount"]
print("Total: " + str(total_amount))
