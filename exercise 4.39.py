# Reverse a given integer number
n=int(input("enter the number: "))

x=str(n)

x=list(x)[::-1]

z=int("".join(x))

print(z)
#print(type(z))