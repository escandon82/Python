# Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs
# number of head-->     1         1
# number of legs-->     4         2
head=int(input("enter the number of heads: "))
legs=int(input("enter the number of legs: "))

if head/legs==0.25:
	number_of_dogs=legs/4
	print("there are ",round(number_of_dogs),'number of dogs')
elif head/legs==0.5:
	number_of_chicken=legs/2
	print("there are ",round(number_of_chicken),'number of chicken')
else:
	print("enter correct numbers")
