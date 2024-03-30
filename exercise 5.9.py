# Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary
def show_employee(name,salary="9000"):
	print("name of employee is {} and his\her salary is {}".format(name,salary))
