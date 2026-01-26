transactions = [
    {"amount": 1200}, # Should be High
    {"amount": 600},  # Should be Medium
    {"amount": 50}    # Should be Low
]

for item in transactions:
    if item["amount"] > 1000:
        print("Amount is High Risk")
    elif item["amount"] > 500:
        print("Amount is Medium Risk")
    else:
        print("Amount is Low Risk")