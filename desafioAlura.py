delivery_distance = 7 #example
is_raining = "yes" #example
delivery_fee = 0

if delivery_distance <= 5:
    delivery_fee = 5

elif delivery_distance > 5  and delivery_distance <= 10:
    delivery_fee = 8

if delivery_distance > 10:
    delivery_fee = 10

if is_raining.lower() == "yes":
    delivery_fee + 2



