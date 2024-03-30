# Turn every item of a list into its square

numbers = [1, 2, 3, 4, 5, 6, 7]

new=[]

for i in numbers:
	x=pow(i,2)
	new.append(x)
 
print(new)

# same using list comprehenssion

result=[pow(x,2) for x in numbers]

print(result)