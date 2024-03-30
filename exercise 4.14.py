# Write a program that will determine weather when the value of temperature and humidity is provided by the user
temp=int(input("enter the value of temp "))
humidity=int(input("enter the value of humidity "))
if temp>=30 and humidity>=90:
	print("Hot and Humid")
elif temp>=30 and humidity<90:
	print("Hot")
elif temp<30 and humidity>=90:
	print("cool and humid")
else:
	print("cool")