# Create an inner function to calculate the addition in the following way
# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate the addition of a and b
# At last, an outer function will add 5 into addition and return it
def outerfunc(n1,n2):
 
 	def innerfunc(n1,n2):
		return n1+n2
 
	add=innerfunc(n1,n2)
 
	return add+5