# Generate 3 random integers between 100 and 999 which is divisible by 5

import random

print("generating three digit number from 100 to 999 which id divisible by 5")

for i in range(3):
	print(random.randrange(100,999,5))