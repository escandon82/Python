# Write a program that will take three digits from the user and add the square of each digit
n=int(input("Enter three digit number: "))
a=n%10  #3
num=n//10  #12
b=num%10  #2
c=num//10  #1
if (a**3 + b**3 + c**3)==n:
	print("the number is armstrong number")
else:
	print("the number is not armstrong number")