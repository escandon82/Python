# Removal all characters from a string except integers
str1 = 'I am 26 years and 10 months old'

str2=str1.split()

new=[]

for i in str2:
	if i.isdigit()==True:
		new.append(i)
 
print("".join(new))