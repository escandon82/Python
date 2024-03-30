# Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

for i in list1:
	for j in list2:
 
 print(i+j)

# using list comprehension

result=[i+j for i in list1 for j in list2]

print(result)
