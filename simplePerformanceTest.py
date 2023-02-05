# Simple Python System Performance Test
# Ryan K., 

import random, sys, os

# Constants
BILLION = 2 ** 30
MILLION = 2 ** 20

# Simple CPU Performance Calculation Function
def cpuCalcTest():
	x, y = -1, 0 	
	num_rolls = 0 
	maxX = 0
	maxY = 0
	print('Calculating rolls...\n')
	while x != y:	
		x = random.randint(1, BILLION)
		if x > maxX:
			maxX = x
		y = random.randint(1, BILLION) # I don't think this is right.  Won't it get stuck in a loop?  There's no chance they will ever be equal.
		if y > maxY:
			maxY = y
		num_rolls += 1

	print(f'x: {x}\n Max x: {maxX}\n y:{y}\n Max y: {maxY}\n Total Rolls: {num_rolls}\n')

cpuCalcTest()``