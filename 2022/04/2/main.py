import os.path

total = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	for pair in [[list(map(int, bounds.split("-"))) for bounds in pair.split(",")] for pair in file.read().splitlines()]:
		sequences = [set(range(bounds[0], bounds[1] + 1)) for bounds in pair]

		if sequences[0] & sequences[1]:
			total += 1
				
print(total)
