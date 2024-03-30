# Write progrme to count the number of vowels in the string
string="Milind Dattatray Mali"
vowel="AEIOUaeiou"

count=0

for i in string:
	if i in vowel:
		count+=1

print(count)