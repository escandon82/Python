# Count the occurrence of each element from a list
# Write a program to iterate a given list and count the occurrence of each element and create a dictionary toshow the count of each element.
list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]

count=dict()

for i in list1:
	if i in count:
		count[i]+=1
	else:
 		count[i]=1
 
print(count)