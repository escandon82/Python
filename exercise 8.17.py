# Logic for quickly swap the first and last number of the list

l1=[1,2,3,4,5]

temp=l1[-1]

l1[-1]=l1[0]

l1[0]=temp

print(l1)