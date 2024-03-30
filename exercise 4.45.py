# Print a pyramid
#n=int(input("enter the number: "))

n=5

for i in range(0,n):
	for j in range(0,n-i):
		print(end=" ")
 
	for k in range(0,i+1):
		print("*",end=" ")
 
	print()