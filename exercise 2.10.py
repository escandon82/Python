# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40R
rad=float(input("enter the radius of cylinder in cm "))
ht=float(input("enter the height of cylinder in cm "))

vol=3.142*(rad**2)*ht
litr=vol/1000
cost=litr*40

print("Volume of cylinder will be ",vol)
print("How much milk we can carry in this cylinder ",litr, 'ltr')
print("this cost of that milk will be",cost)