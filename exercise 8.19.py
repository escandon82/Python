# Create lambda function for the sum of all the elements in the list

l1=[5,8,10,20,50,100]

from functools import reduce

result=reduce(lambda x,y:x+y, l1)

print(result)