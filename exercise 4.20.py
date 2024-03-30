# Write a program that can multiply 2 numbers provided by the user without using the * operator
x=int(input("enter the first number: "))  #2 
y=int(input("enter the seconde number "))   #3

result=0

for i in range(0,y):
	result=result+x
print(result)