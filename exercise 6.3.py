# Write a program to remove characters from a string starting from zero up to n and return a new string
def remove (word,n):
 
	x=len(word)
	p=list(word)

	for i in p:
		if n<=x:
			z=word[n:]
 	print(z)
  
remove("pynative",2)