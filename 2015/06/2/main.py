import itertools
import os.path

grid = [[0 for _ in range(1000)] for _ in range(1000)]

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	instructions = [instruction.split() for instruction in file.read().splitlines()]
	
	for instruction in instructions:
		for y in range(int(instruction[-3].split(",")[1]), int(instruction[-1].split(",")[1]) + 1):
			for x in range(int(instruction[-3].split(",")[0]), int(instruction[-1].split(",")[0]) + 1):
				if instruction[0] == "toggle":
					grid[y][x] += 2
				elif instruction[1] == "off":
					grid[y][x] -= min(grid[y][x], 1)
				else:
					grid[y][x] += 1

print(sum(itertools.chain.from_iterable(grid)))
