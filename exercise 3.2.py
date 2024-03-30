# Read content from the file
filename="siddharth.txt"
with open(filename) as f_obj:
	content=f_obj.read()
	print(content)
