# Write a program to display only those numbers from a list that satisfy the followingconditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
num=[12,75,150,180,145,525,50]

for i in num:
	if i>500:
		break
	elif i>150:
		continue
	else:
		if i%5==0:
			print(i)