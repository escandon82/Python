# Write a program to check if the given number is a palindrome number
n=input("enter the number: ")
rev_number=n[::-1]
print(rev_number)

if n==rev_number:
	print("the given number is palindrom")
else:
	print("the given number is not palindrom")
