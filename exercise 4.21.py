# Write a program that can find the factorial of a given number provided by the user
n=int(input("enter the number : "))

factorial=1

if n < 0 :
	print("factorial dont exist for negative number")
elif n==0:
	print("for zero factorial is always one")
else:
	for i in range(1,n+1):
		factorial=factorial*i
	print(factorial)