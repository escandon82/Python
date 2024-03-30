# Collecting arbitrary number of arguments
def make_pizza(size,*toppings):
	print(f"making {size} pizza")
	print("toppings: ")
	for i in toppings:
		print(i)