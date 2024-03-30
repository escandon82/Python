# Write a python program to remove all the duplicates from a list

l1=[1,2,3,3,3,4,4,5,6,7,8,9,9]
l2=[]

for i in l1:
	if i not in l2:
		l2.append(i)
 
print(l2)