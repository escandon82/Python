# Write a program to print whether a given number is prime number or not
x=int(input("enter the number: "))
new=[]
if x==1:
	print("1 is not prime number")
else:
	for i in range(1,x+1):
		if x%i==0:
			new.append(i)
			#print(new)
			
    if len(new) > 2:
    	print("it is not a prime number")
    else:
    	print("it is prime number ")