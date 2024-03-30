# The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 year
p=10000
for i in range(1,10):
	p=p-0.1*p
	print(round(p),end=" ")