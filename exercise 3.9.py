# Using else block
x=int(input("enter the number: "))
y=int(input("enter the number: "))
try:
	result=x/y
except ZeroDivisionError:
	print("hey you...denominater cant be zero")
else:
	print(result)

# create simple calculater
print("enter the numbers: ")
print("enter the 'q' to exit")
while(True):
	x=input("enter the number:")
	if x=='q':
		break
		y=input("enter the number:")
		if y=='q':
			break
			try:
				result=int(x)/int(y)
			except ZeroDivisionError:
				print("bhidu zero se divide nahi kar sakate")
			else:
				print(result)