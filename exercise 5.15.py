# First 25 prime number
# first we will write code for getting prime number

a=23

new=[]

for i in range(1,a+1):
	if a%i==0:
		new.append(i)
 
if len(new)>2:
	print("it's not a prime number")
else:
	print("it's prime number")

# to get first 25 numbers
def is_prime(x):
	new=[]
	if x<=1:
		return false
	else:
		for i in range(1,x+1):
			if x%i==0:
				new.append(i)
	#print(new) 
	if len(new)<=2:
		return True
	else:
		return False
 
#now will write the main code
count=0
num=2

while count<25:
	if is_prime(num)==True:
		print(num,end=" ")
		count+=1
 
	num+=1
