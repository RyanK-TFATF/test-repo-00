# Simple Python System Performance Test
# Ryan K., 

import random, sys, os

# Constants
BILLION = 2 ** 30
MILLION = 2 ** 20

# Simple CPU Performance Calculation Function
def cpuCalcTest():
	# Generate Random Numbers Until Match
	x, y = -1, 0 	
	num_rolls, maxX, maxY = 0, 0, 0 	
	print('Calculating rolls...\n')
	while x != y:	
		x = random.randint(1, MILLION ** 2)
		if x > maxX:
			maxX = x
		y = random.randint(1, MILLION ** 2) # I don't think this is right.  Won't it get stuck in a loop?  There's no chance they will ever be equal.
		if y > maxY:
			maxY = y
		num_rolls += 1
	print(f'Match: {x, y}\nMax x: {maxX}\nMax y: {maxY}\nTotal Rolls: {num_rolls}\n')
	# Subtraction Speed Test
	print('Subtracting rolls back to 0.\n')
	while x > -MILLION and y > -MILLION:
		x += -1
		y += -1
	print(f'Finished subtracting. Final Values: {x, y}\n')

cpuCalcTest()