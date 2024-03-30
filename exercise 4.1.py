# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

prev_num=0
for i in range(0,11):
	x=i+prev_num
	prev_num=i
	
	print(x,end=" ")
