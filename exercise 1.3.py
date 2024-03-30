# Write a program that will give you the sum of 3 digits
x=int(input("enter three digit number"))
a=x%10   # we will get last digit
num=x//10  # integer-divison here we will get first two digit
b=num%10   # here we will get last digit of two digit number
c=num//10 # here will get first digit of two digit number
print(a+b+c)