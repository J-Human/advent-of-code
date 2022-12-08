import os.path

total = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	rows = [[int(height) for height in row] for row in file.read().splitlines()]
	
	for y in range(0, len(rows)):
		for x in range(0, len(rows[y])):
			n = [rows[n][x] for n in range(0, y)]
			s = [rows[n][x] for n in range(y + 1, len(rows))]
			w = rows[y][:x]
			e = rows[y][x + 1:]

			if any(axis in (0, len(rows) - 1) for axis in (y, x)) or any(max(direction) < rows[y][x] for direction in [n, s, e, w]):
				total += 1
	
print(total)
