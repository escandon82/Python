# Given two integer numbers return their product only if the product is equal to or lowerthan 1000, else return their sum
num1=int(input("enter the number: " ))
num2=int(input("enter the number: " ))

def mul_sum_int(num1,num2):
	#calculate product of two number
	mul=num1*num2
	total=num1+num2
	#checking if product is less than 1000
	if mul<=1000:
		return mul
	else:
 		return total
 
print(mul_sum_int(num1,num2))