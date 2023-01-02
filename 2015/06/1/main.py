import itertools
import os.path

grid = [[0 for _ in range(1000)] for _ in range(1000)]

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	instructions = [instruction.split() for instruction in file.read().splitlines()]
	
	for instruction in instructions:
		for y in range(int(instruction[-3].split(",")[1]), int(instruction[-1].split(",")[1]) + 1):
			for x in range(int(instruction[-3].split(",")[0]), int(instruction[-1].split(",")[0]) + 1):
				if instruction[0] == "toggle":
					grid[y][x] = not grid[y][x]
				elif instruction[1] == "off":
					grid[y][x] = 0
				else:
					grid[y][x] = 1

print(len(list(filter(lambda cell: cell, itertools.chain.from_iterable(grid)))))
