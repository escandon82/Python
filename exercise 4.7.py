# Print all the armstrong numbers in the range of 100 to 100
armstrong_list=[]
for i in range(100,1000):
	a=i%10  # 123-->3
	num=i//10 #123-->12
	b=num%10  #--->2
	c=num//10  #-->1

	if (a**3)+(b**3)+(c**3)==i:
		armstrong_list.append(i)
print(armstrong_list)