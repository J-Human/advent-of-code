import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	cubes = [tuple(map(int, line.split(","))) for line in file.read().splitlines()]
	total = 0
	offsets = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
	
	for x, y, z in cubes:
		for possible in [(x + dx, y + dy, z + dz) for dx, dy, dz in offsets]:
			if possible in cubes:
				total += 1
				
	print((len(cubes) * 6) - total)
