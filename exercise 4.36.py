# Write a program to display all prime numbers within a range
def prime(n):
 
	if n<=1:
		return False
	else:
		l1=[]
 
		for i in range(1,n+1):
			if n%i==0:
				l1.append(i)
 
		#print(l1)
 
 		if len(l1)<=2:
 			return True
 		else:
			return False
 
inp1=int(input("enter the number : "))
inp2=int(input("enter the number : "))

for i in range(inp1,inp2+1):
	if prime(i)==True:
		print(i,end=" ")
