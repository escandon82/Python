# Roll dice in such a way that every time you get the same number

# Dice has 6 numbers (from 1 to 6). Roll dice in such a way that every time you must get the same output number. do this 5 times.

import random
dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
for i in range(5):
	random.seed(25)
	print(random.choice(dice))