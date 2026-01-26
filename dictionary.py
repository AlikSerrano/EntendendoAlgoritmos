transaction = {
    "amount": -5000, 
    "currency": "BRL", 
    "status": "pending"
}

if abs(transaction["amount"]) > 1000 and (transaction["currency"]) == "BRL":
    print("Flag for review!")
                                          