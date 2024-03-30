# Write a program that take a user input of three angles and will find out whether it can form a triangle or not
# since sum of all the angle of trianle is 180 deg
a=float(input("1st angle of triangle: "))
b=float(input("2nd angle of triangle: "))
c=float(input("3rd angle of triangle: "))

if (a+b+c)==180 and a!=0 and b!=0 and c!=0:
	print("yes it can form a triangle")
else:
	print("No it cant form a triangle")
