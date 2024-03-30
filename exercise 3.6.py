# Write all content of a given file into a new file by skipping line number 5
#read test file
with open ("test file.txt",'r') as fp:

#read all the lines from the file
lines=fp.readlines()

#open new file in write mode
with open ("test file new.txt","w") as fp:
count=0
#iterate each line from test file
for line in lines:
	if count==4:
		count=+1
		continue
	else:
		fp.write(line)
		count+=1