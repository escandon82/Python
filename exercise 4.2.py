# Write a python program to search a given number from a list
l1=[4,5,6,2,3,9,1,4,5,6,3]
n=int(input("enter the number: "))
for i in l1:
	if i==n:
		print("Number exist")
		break
	else:
		print("number dont exist")