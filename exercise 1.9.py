# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not
n=int(input("Enter Four digit number: "))
#1234
a=n%10  #4
num=n//10  #123 
b=num%10  #3
num_1=num//10  #12
c=num_1%10 #2 
d=num_1//10  #1
if (a**4 + b**4 + c**4+d**4)==n:
	print("the number is narcissist number") 
else:
	print("the number is not narcissist number")