# Writing multiple line to empty file
with open(filename,'w') as f:
	f.write("Deep learning is awesome.\n")
	f.write("AI is future\n")

with open(filename,'a') as f:
	f.write("i love to work with data science projects \n")
	f.write("i love making the application")

### syntax for opening the file using path
filename="< file path >"
with open(filename) as f:
	lines=f.readlines()