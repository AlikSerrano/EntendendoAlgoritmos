

def check_transactions(amount):
    if amount > 2000:
        print("Possible Fraud")
    else:
        print("Aproved")

transactions_list = [50, 10000, 30, 5000, 450]

print("--- STARTING BATCH CHECK ---")

for t in transactions_list:
    print("Analyzing transaction of:", t)
    check_transactions(t)
print("---")

