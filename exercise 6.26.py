# Extract all the emailid for the given string
string="Hi my name is Govind Das and my mail id is milindmali108@gmail.com and my org mai

new=list(string.split())
for i in new:
	if ".com" in i:
		print(i)