# Split the array into four equal-sized sub-arrays
# Note: Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays

new_array=np.arange(10,34,1)
new_array=new_array.reshape(8,3)
print(new_array)

# now to divide array into 4 equal division

subarray=np.split(new_array,4)

print("="*100)

print(subarray)