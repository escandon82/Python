# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit
cost=int(input("what is cost of product: "))
sell=int(input("what is sell price of product: "))

if (sell-cost)>0:
	amount=sell-cost
	print("it is profit by ",amount)
else:
	amount=sell-cost
	print("it is loss by ",amount)