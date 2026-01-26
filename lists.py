transactions = [50, -20, 100, -5, -10, 200]
large_tranfers=[]

for number in transactions:
    if number > 80:
        large_tranfers.append(number)
print(large_tranfers)