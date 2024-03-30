# Read line number 4 from the following file
with open("test file.txt","r") as fp:
	lines=fp.readlines()
	print(lines[3])
