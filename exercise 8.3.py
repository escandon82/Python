# Take a number from the user and find the number of digits in it

n=int(input("enter the number: "))

digit_list=list(map(int,str(n)))

print(digit_list)

print(len(digit_list))