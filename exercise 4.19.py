# Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55
user_input=int(input("enter the number: "))

x=0

for i in range(1,user_input+1):
	x=x+i
print(x)