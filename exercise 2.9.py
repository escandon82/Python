# Write a program to find the simple interest when the value of principle,rate of interest and time period is given
P =float(input("principle amount: "))
R =float(input("Rate of interest: "))
T =int(input("for the time period: "))
Simple_interest= (P*R*T)/100
print(Simple_interest)
total_due=P+Simple_interest
print("Total due amount will need to pay wll be ",total_due)
