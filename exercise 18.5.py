# Generate random String of length 5

import random
import string

def randomstring(stringLength):
	"""gernerate random string of five characters"""
 
	letters=string.ascii_letters
	return "".join(random.choice(letters) for i in range(stringLength))

print("random string is ",randomstring(5))