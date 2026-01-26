transfers = [
    {"amount": 5000, "currency": "EUR"},    # High Value -> Bucket 1
    {"amount": -10, "currency": "RUB"},     # Suspicious Currency -> Bucket 2
    {"amount": -2500, "currency": "USD"},   # High Value -> Bucket 1
    {"amount": 100, "currency": "GBP"},     # Normal -> Bucket 3
    {"amount": 50, "currency": "TRY"}       # Suspicious Currency -> Bucket 2
]

high_value = []
manual_review = []
approved = []

for item in transfers:
    if abs (item["amount"]) > 2000:
        high_value.append(item)
      
    elif item["currency"] == "RUB" or item["currency"] == "TRY":
        manual_review.append(item)
     
    else:
        approved.append(item)
    
print(high_value)
print(manual_review)
print(approved)