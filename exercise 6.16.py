# Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters
str1 = "PYnative29@#8496"
str2=list(str1)

total=0
counter=0

for i in str2:
	if i.isdigit()==True:
		total=total+int(i)
		counter+=1
 
print("sum of digits in the given string is ",total)
print("avg of digits in the given string is ",round(total/counter,2))