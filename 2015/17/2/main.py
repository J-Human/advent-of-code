import itertools
import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	containers = list(map(int, file.read().splitlines()))
	valid = []
	
	for i in range(len(containers)):
		for combination in itertools.combinations(containers, i):
			if sum(combination) == 150:
				valid.append(len(combination))
	
	print(min(valid))
	