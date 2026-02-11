incoming_command = "insert 0 50"
parts = incoming_command.split()
print(parts)

text_position = parts[1]
real_position = int(text_position)

print("Original:", text_position, type(text_position))
print("Converted:", real_position, type(real_position))

database = []
incoming_command = "insert 0 50"
parts = incoming_command.split()

verb = parts[0]
position = int(parts[1])
value = int(parts[2])

if verb == "insert":
    print("I detected an INSERT command.")
    database.insert(position, value)
    print("Command executed successfully.")
print ("Final Database:", database)

                      