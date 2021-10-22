# Test Python Script

import random

print("Time to roll the dice!\n") # Fixed a typo. 
x = random.randint(1, 100)
y = random.randint(-1, -100) # Is this right?



while x != y:
	print(f"x equals [x] and y equals [y].\n")
	x = random.randint(1, 100)
	y = random.randint(-1, -100) # I don't think this is right.  Won't it get stuck in a loop?  There's no chance they will ever be equal.
