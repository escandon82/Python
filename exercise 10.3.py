# Get Only unique items from two sets
# Write a Python program to return a new set with unique items from both sets by removing duplicates

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3=set1.union(set2)

print(set3)