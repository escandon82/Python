# Write a program to count the total number of digits in a number using a while loop.
n=input("enter the number: ")
x=list(n)

count=0

while count<len(x):
	for i in x:
		count+=1
print(count)