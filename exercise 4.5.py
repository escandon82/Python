# Calculate income tax for the given income by adhering to the below rules
# first 10k--> 0%
# second 10 --> 10%
# remaining-->20%

n=int(input("enter the number: "))
if n<=10000:
	print(n)
else:
	a=n-10000
	b=a-10000
	c=b*0.2
	d=c+1000
	print(d)
