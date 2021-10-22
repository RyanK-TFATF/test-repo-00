# Test Python Script

import random

print("Time to roll the dice!\n") # Fixed a typo. 
x = random.randint(1, 50)
y = random.randint(1, 50) # Is this right?
# No, it wasn't right.  Thank you for catching it! 



while x != y:
	print(f"x equals {x} and y equals {y}.\n")  # The variable formatting was right though.  Thanks! 
	x = random.randint(1, 50)
	y = random.randint(1, 50) # I don't think this is right.  Won't it get stuck in a loop?  There's no chance they will ever be equal.
