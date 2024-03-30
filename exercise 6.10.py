# Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a program to arrange thecharacters of a string so that all lowercase letters should come first
string="PyNaTive"

cap=list(string.upper())
sma=list(string.lower())

new=[]

l1=list(string)

for i in l1:
	if i in sma:
		new.append(i)
 
for i in l1:
	if i in cap:
		new.append(i)
 
result="".join(new)
 
print(result)

# anther way of doing the same thing
given="PyNaTive"

x=given.upper()

l1=[]

for i in given:
	if i not in x:
		l1.append(i)
for i in given:
	if i in x:
		l1.append(i)
 
result="".join(l1)

print(result)