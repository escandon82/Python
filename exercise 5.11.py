# Create a recursive function
# A] Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself again and again
def addition(num):
	if num==0:
		return 0
	else:
		return num+addition(num-1)

# B] Write a program to create a recursive function to calculate the factorial of numbers from 0 to10
def factorial(num):
	if (num==1):
		return 1
	else:
		return num*factorial(num-1)