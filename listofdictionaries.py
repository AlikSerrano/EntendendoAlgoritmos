history = [
    {"amount": 50, "currency": "USD"},
    {"amount": -5000, "currency": "BRL"},
    {"amount": 2000, "currency": "USD"},
    {"amount": -10, "currency": "EUR"}
]

suspicious=[]

# Loop through the list (The Conveyor Belt)
for money in history:
    # Check the SINGLE item (The Box)
    # 1. Use abs() for the amount
    # 2. Use money["currency"] to look at the specific tag
    if abs (money["amount"]) > 1000 and money["currency"] == "BRL":
        # Add ONLY the single item to your list
        suspicious.append(money)
print("Suspicious BRL transaction found!")
print(suspicious)