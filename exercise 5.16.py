# Print the first 20 numbers of a Fibonacci series
n=int(input("enter the number: "))

def fibonacci(n):
 	a=0
	b=1
	count=0
 
	if n<=0:
		print("You can enter only Positive integer values")
	elif n==1:
		print(a)
	else:
		while count<n:
			print(a,end=' ')
			c=a+b
			a=b
			b=c
 
			count+=1
 
 fibonacci(n)