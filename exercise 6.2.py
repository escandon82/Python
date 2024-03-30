# Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number
string=input("enter the text: ")

x=list(string)

print(string)

for i in x[0::2]:
	print(i,end=" ")

