# Find the reverse of a number provided by the user(any number of digit)

n=int(input("enter the number: "))

digit_list=list(map(int,str(n)))

digit_list=digit_list[::-1]

num=int("".join(map(str,digit_list)))

print(num)