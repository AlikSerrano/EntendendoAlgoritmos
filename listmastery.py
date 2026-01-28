# list_mastery.py
# Simulating the logic from the Slack snippet

# 1. Start with an empty list
my_list = []

print("--- STARTING LIST OPERATIONS ---")

# Command: insert 0 5 (Insert number 5 at position 0)
my_list.insert(0, 5)
print("1. Inserted 5 at pos 0:", my_list)

# Command: insert 1 10 (Insert number 10 at position 1)
my_list.insert(1, 10)
print("2. Inserted 10 at pos 1:", my_list)

# Command: insert 0 6 (Insert number 6 at position 0)
my_list.insert(0, 6)
print("3. Inserted 6 at pos 0:", my_list)

# Command: print
print("4. Current List:", my_list)

# Command: remove 6 (Remove the first number 6 found)
my_list.remove(6)
print("5. Removed number 6:", my_list)

# Command: append 9 (Add 9 to the end)
my_list.append(9)
print("6. Appended 9:", my_list)

# Command: append 1 (Add 1 to the end)
my_list.append(1)
print("7. Appended 1:", my_list)

# Command: sort (Organize small to big)
my_list.sort()
print("8. Sorted List:", my_list)

# Command: pop (Remove the last item)
my_list.pop()
print("9. Popped last item:", my_list)

# Command: reverse (Flip it backwards)
my_list.reverse()
print("10. Reversed List:", my_list)