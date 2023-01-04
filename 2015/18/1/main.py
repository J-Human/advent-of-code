import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	grid = list(map(list, file.read().splitlines()))
	next_status = {}
	offsets = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
	
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			next_status[(x, y)] = grid[y][x]

	for _ in range(100):
		for x, y in next_status:
			neighbors = [grid[y + dy][x + dx] for dx, dy in offsets if (x + dx, y + dy) in next_status]
			
			if grid[y][x] == "#":
				condition = len(list(filter(lambda cell: cell == "#", neighbors))) in (2, 3)
				next_status[(x, y)] = [".", "#"][condition]
			else:
				condition = len(list(filter(lambda cell: cell == "#", neighbors))) == 3
				next_status[(x, y)] = [".", "#"][condition]

		for (x, y), status in next_status.items():
			grid[y][x] = status

	print(sum([len([cell for cell in grid[y] if cell == "#"]) for y in range(len(grid))]))
