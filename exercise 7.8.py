# Get all values from the dictionary and add them to a list but don’t add duplicates
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 5
speed_list=[]

for value in speed.values():
	if value not in speed_list:
		speed_list.append(value)
 
print(speed_list)