# Write a menu driven program -
# 1.cm to ft
# 2.kl to miles
# 3.usd to inr
# 4.exit
user_input=int(input("""Enter 1 to 'cm' to 'ft' Enter 2 to 'km' to 'miles' Enter 3 to  'USD' to 'INR' Enter 4 to exit """))

if user_input==1:
	var1=int(input("enter the value in cm"))
	output=var1/30.48
	print(output,'ft')
elif user_input==2:
	var2=int(input("enter the value in km"))
	output=var2/1.609
	print(output,'miles')
elif user_input==3:
	var3=int(input("enter the value in usd"))
	output=var3*81.80
	print(output,"Inr")
else:
	print("Exit")