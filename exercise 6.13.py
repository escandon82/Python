# String characters balance Test
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all thecharacters in the s1 are present in s2. The character’s position doesn’t matter
s1 = "Yn"
s2 = "PYnative"

count=0

for i in s1:
	if i in s2:
		count+=1
 
if len(s1)==count:
	print("s1 and s2 are balanced")
else:
	print("s1 and s2 are not balanced")