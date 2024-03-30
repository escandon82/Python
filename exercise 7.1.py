# Create a list by picking an odd-index items from the first list and even index items fromthe second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

l3=[]

for i in l1[1::2]:
	l3.append(i)
for i in l2[0::2]:
	l3.append(i)
 
print(l3)