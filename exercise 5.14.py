# Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2,65]

y=0

for i in x:

	if i > y:
		y=i

print(y)

print(max(x))