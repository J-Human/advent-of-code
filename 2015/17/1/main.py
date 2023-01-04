import itertools
import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	containers = list(map(int, file.read().splitlines()))
	total = 0
	
	for i in range(len(containers)):
		for combination in itertools.combinations(containers, i):
			if sum(combination) == 150:
				total += 1
	
	print(total)
	