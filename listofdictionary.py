transfers = [
    {"id": 101, "status": "completed", "amount": 500},
    {"id": 102, "status": "failed", "amount": 20},
    {"id": 103, "status": "completed", "amount": 1000},
    {"id": 104, "status": "failed", "amount": 150}
]

failed_transfers=[]

for item in transfers:
    if item["status"] == "failed":
       failed_transfers.append(item)
print(failed_transfers)

completed_transfers=[]

for item in transfers:
    if item["status"] == "completed":
        completed_transfers.append(item)
print(completed_transfers)