# Print Pascal Triangle
n=int(input("enter the number: "))

list1=[]

for i in range(0,n):
	temp=[]
	for j in range(0,i+1):
		if j==0 or j==i:
			temp.append(1)
		else:
			temp.append(list1[i-1][j]+list1[i-1][j-1])
	list1.append(temp)
 
#print(list1)

for i in range(n):
	for j in range(0,n-i-1):
		print(" ",end="")
 
	for j in range(0,i+1):
		print(list1[i][j],end=" ")
 
	print()