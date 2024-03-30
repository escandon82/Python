# Break down the list into equal number of chucks

l1=[1,2,3,4,5,6,7,8,9,10,11,12]

chunk=3

output=[l1[i:i+chunk] for i in range(0,len(l1),chunk)]

print(output)