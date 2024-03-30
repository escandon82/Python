# Write a program that will reverse a four digit number.Also it checks whether the reverse
x=int(input("enter the four digit number "))
a=x%10  # to get last number
num_1=x//10 # to get first three numbers
b=num_1%10   # this way i will get 2nd last number
num_2=num_1//10  # here will get first two digit number
c=num_2%10  # we will get 2 nd number
d=num_2//10  # here we will get 1st digit
#formula for reverse
rev=a*1000+b*100+c*10+d
print(rev)
#now let check whether both number are equal or not
if x==rev:    print(True) else:    print(False)