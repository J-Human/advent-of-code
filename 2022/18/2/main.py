import collections
import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	cubes = [tuple(map(int, line.split(","))) for line in file.read().splitlines()]
	total = 0
	offsets = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
	
	max_x, max_y, max_z = [max(x for x, _, _ in cubes), max(y for _, y, _ in cubes), max(z for _, _, z in cubes)]
	min_x, min_y, min_z = [min(x for x, _, _ in cubes), min(y for _, y, _ in cubes), min(z for _, _, z in cubes)]

	visited = set()
	queue = collections.deque([(min_x - 1, min_y - 1, min_z - 1), (min_x, min_y, min_z)])
	total = 0
	
	while queue:
		x, y, z = queue.popleft()
		
		if (x, y, z) not in visited:
			for nx, ny, nz in [(x + dx, y + dy, z + dz) for dx, dy, dz in offsets]:
				if nx not in range(min_x - 1, max_x + 2) or ny not in range(min_y - 1, max_y + 2) or nz not in range(min_z - 1, max_z + 2):
					continue

				if (nx, ny, nz) in cubes:
					total += 1
				else:
					queue.append((nx, ny, nz))

			visited.add((x, y, z))

	print(total)
