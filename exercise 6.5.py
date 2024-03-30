# Count the frequency of a particular character in a provided string. Eg 'hello how are you'is the string, the frequency of h in this string is 2
a=input("enter the text: ")
b=input("enter the character: ")

count=0

for i in a:
	if i in b:
		count=count+1
 
print("frequency of searched character is ",count,"times")