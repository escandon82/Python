# Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then thelast char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go atthe end of the result.
s1="ABC"
s2="xyz"

a=s1[0]
b=s1[len(s1)//2]
c=s1[-1]

x=s2[0]
y=s2[len(s2)//2]
z=s2[-1]

result="".join([a,z,b,y,c,x])
print(result)