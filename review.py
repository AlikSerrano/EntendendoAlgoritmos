# 1. Start with an empty bank line
bank_line = []

# 2. Two people join the END of the line (Append)
bank_line.append(100)
bank_line.append(200)

# 3. A VIP customer cuts to the FRONT (Position 0) (Insert)
bank_line.insert(0, 50)

# 4. The person at the very back gets tired and leaves (Pop)
bank_line.pop()

# --- NOW THE SYSTEM RECEIVES A TEXT MESSAGE ---
incoming_message = "remove 100"

# 5. Cut the text message into pieces (The Knife)
parts = incoming_message.split() 

# 6. Grab the second word ("100") and convert it to a real number
value_to_remove = int(parts[1])

# 7. Search the line and remove that specific number
bank_line.remove(value_to_remove)

# 8. Print the final result
print("Who is left in line?", bank_line)