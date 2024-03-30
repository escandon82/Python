# Return a set of elements present in Set A or B, but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference(set2)

# Check if two sets have any elements in common. If yes, display the common elements

set1 = {10 ,20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
	print("above two set dont have any common element")
else:
	print(set1.intersection(set2))