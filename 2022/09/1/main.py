import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	visited = set([(0, 0)])
	hx, hy = [0, 0]
	tx, ty = [0, 0]

	for instruction in file.read().splitlines():
		direction, amount = instruction.split(" ")
		
		for _ in range(int(amount)):
			hx += -1 if direction == "L" else direction == "R"
			hy += -1 if direction == "D" else direction == "U"
			
			dx, dy = hx - tx, hy - ty
			if abs(dx) > 1 or abs(dy) > 1:
				tx += 1 if dx > 0 else (0 if dy and not dx else -1)
				ty += 1 if dy > 0 else (0 if dx and not dy else -1)

			visited.add((tx, ty))

	print(len(visited))
