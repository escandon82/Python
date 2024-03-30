#  Write a program to print all the unique combinations of two digits from 1 to 4 for ex (1,2), (2,3).....
# since we have 4 digit there unique combination will be 16 
for i in range(1,5):
	for j in range(1,5):
		if i != j:
			print(i,j)