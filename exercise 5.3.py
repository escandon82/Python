# Write a function to return True if the first and last number of a given list is same. Ifnumbers are different then return False.
l1=[1,2,3,4,5,1]

num1=l1[0]
num2=l1[-1]

def xyz(list):
	if num1==num2:
		return True
	else:
		return False
 
xyz(l1)