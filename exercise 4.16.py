# -Write a program that will give you the in hand salary after deduction of HRA(10%),
# DA(5%),
# PF(3%),
# and tax
# (if salary is between 5-10 lakh–10%),
# (11-20lakh–20%),
# (20< _ – 30%)
# (0-1lakh print k)

salary=int(input("enter the salary amount: "))
if salary in range(500000,1000000):
	salary=salary-salary*0.1
elif salary in range(1100000,2000000):
	salary=salary-salary*0.2
elif salary> 2000000:
	salary=salary-salary*0.3
else:
	print("no tax")

print("Salary after tax cutting",salary)

HRA=salary*0.10   # 63000
DA=salary*0.05   #31500
PF=salary*0.03   #18900

remain=salary-(HRA+DA+PF)

#print("in hand salary after HRA/DA/PF cutting",remain)

if remain in range(1000,99999):
	print("in hand salary after tax/HRA/DA/PF cutting",remain/1000,"k")
elif remain in range(100000,9999999):
	print("in hand salary after tax/HRA/DA/PF cutting",remain/100000,"lakh")
else:
	print("in hand salary after tax/HRA/DA/PF cutting",remain/10000000,"Cr")
