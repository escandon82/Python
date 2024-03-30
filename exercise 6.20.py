# Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

for i in str_list:
	if i == "" or i==None:
		str_list.remove(i)

print(str_list)