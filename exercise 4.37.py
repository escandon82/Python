# Display Fibonacci series up to 10 terms
n=int(input("enter the number: "))

num1=0
num2=1

print(num1,end=" ")
print(num2,end=" ")

for i in range(0,n):
 
	num3=num1+num2
	num1=num2
	num2=num3

 	print(num3,end=" ")