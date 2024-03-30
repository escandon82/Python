# Write a program that can perform union and intersection on 2 given list

l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
uni=[]
inter=[]

for i in l1:
	if i in l2:
		inter.append(i)
 
print(inter)

for i in l1:
	if i not in uni:
		uni.append(i)
 
for i in l2:
	if i not in uni:
		uni.append(i)
 
print(uni)