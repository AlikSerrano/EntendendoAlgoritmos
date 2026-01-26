transactions = [50, -20, 100, -5, -10, 200, -90]

items = []

for number in transactions:
    if abs(number)>80:
        items.append(number)
print(items)