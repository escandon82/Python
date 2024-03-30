# Remove duplicates from a list and create a tuple and find the minimum and maximumnumber
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

list1=set(sample_list) # removed all the duplicates

tuple1=tuple(list1)

print("Unique element in the sample list:\n",tuple1)
print("Maximum number in the sample list:\n",max(tuple1))
print("Minimun number in the sample list:\n",min(tuple1))