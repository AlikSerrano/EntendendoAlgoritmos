transactions = [
    {"id": 1, "currency": "USD", "amount": 100},
    {"id": 2, "currency": "BRL", "amount": 50},
    {"id": 3, "currency": "EUR", "amount": 20},
    {"id": 4, "currency": "GBP", "amount": 10}
]

international=[]

for item in transactions:
    if item["currency"] == "USD" or item["currency"] == "EUR":
        international.append(item)
print(international)
print("International transactions found!")