import collections
import os.path
import sys

def bfs(grid, start, end):
	visited = set([start])
	queue = collections.deque([(0, start)])
	distance = 0
	
	while queue:
		distance, (lx, ly) = queue.popleft()

		for nx, ny in [(lx + 1, ly), (lx - 1, ly), (lx, ly + 1), (lx, ly - 1)]:
			if nx not in range(len(grid[0])) or ny not in range(len(grid)):
				continue
			elif (nx, ny) in visited or ord(grid[ny][nx]) - ord(grid[ly][lx]) > 1:
				continue		
			elif (nx, ny) == end:
				return distance + 1

			visited.add((nx, ny))
			queue.append((distance + 1, (nx, ny)))

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	grid = [list(row) for row in file.read().splitlines()]
	end = (0, 0)
	possible_starts = []

	for y, row in enumerate(grid):
		for x, column in enumerate(row):
			if column == "E":
				end = (x, y)
				grid[y][x] = "z"
			elif column == "S":
				possible_starts.append((x, y))
				grid[y][x] = "a"
			elif column == "a":
				possible_starts.append((x, y))

	print(min([result for result in [bfs(grid, start, end) for start in possible_starts] if result]))
