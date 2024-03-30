# Write a program to print the first 25 odd numbers
# get me first 25 odd number
# i dont know how many time loop will run--> while loop
flag=0
i=1

odd_list=[]

while True:
	if i%2 != 0:
		odd_list.append(i)
		flag=flag+1
 	if flag==25:
 		break
 	i=i+1

print(odd_list)