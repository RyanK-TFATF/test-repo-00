# Test Python Script

import random

prant("Time to roll the dice!\n")
x = random.randint(1, 100)
y = random.randint(-1, -100)

while x != y:
	print(f"x equals {x} and y equals {y}.\n")
	x = random.randint(1, 100)
	y = random.randint(1, 100)
