# How does finally block work in pytho
# no matter what if your exception cought or not your finally code always executed
try:
	print(5/2)
except ZeroDivisionError:
	print("you cant divide by zero")
finally:
	print("Hip Hip hurray!!")
