import math
import os.path

def take_until_above(numbers, maximum):
	final = []
	
	for n in numbers:
		final.append(n)
		if n >= maximum:
			break

	return final
	

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	rows = [[int(height) for height in row] for row in file.read().splitlines()]
	score = 0
	
	for y in range(0, len(rows)):
		for x in range(0, len(rows[y])):
			n = reversed([rows[n][x] for n in range(0, y)])
			s = [rows[n][x] for n in range(y + 1, len(rows))]
			w = reversed(rows[y][:x])
			e = rows[y][x + 1:]
			
			score = max(score, math.prod([len(take_until_above(direction, rows[y][x])) for direction in [n, s, e, w]]))

	print(score)
