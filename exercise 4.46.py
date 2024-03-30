# Write a program to print the following start pattern using the for loop
n=int(input("enter the number: "))

for i in range(1,n+1):
	for j in range(1,i+1):
		print("*",end=" ")
	print("\n")
 
for i in range(n-1,0,-1):
	for j in range(0,i):
		print("*",end=" ")
	print("\n")