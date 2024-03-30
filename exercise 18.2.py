# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

# Note you must adhere to the following conditions:
# The lottery number must be 10 digits long.
# All 100 ticket number must be unique.

import random

lottery_tickets_list = []
print("creating 100 random lottery tickets")
# to get 100 ticket
for i in range(100):
	# ticket number must be 10 digit (1000000000, 9999999999)
	lottery_tickets_list.append(random.randrange(1000000000, 9999999999))
# pick 2 luck tickets
winners = random.sample(lottery_tickets_list, 2)
print("Lucky 2 lottery tickets are", winners)