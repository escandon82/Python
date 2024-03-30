# Check if all items in the tuple are the same

t = (45, 45, 45, 45)

#to check whether all the item are same
all_same=all(i==t[0] for i in t)

if all_same:
	print("yes all the item are same in the given tuple")
else:
	print("No all the item are not same in the given table")