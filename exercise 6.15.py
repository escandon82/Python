# Write a python program to convert a string to title case without using the title()
a=input("enter the title: ")
b=a.split()

r=''

#print(b)

for i in b:
	r=r+i.capitalize()+" "
 
print(r)