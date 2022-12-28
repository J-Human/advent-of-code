import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	visited = set([(0, 0)])
	rope = [[0, 0] for _ in range(10)]

	for instruction in file.read().splitlines():
		direction, amount = instruction.split(" ")
		
		for _ in range(int(amount)):
			rope[0][0] += -1 if direction == "L" else direction == "R"
			rope[0][1] += -1 if direction == "D" else direction == "U"
			
			for i in range(9):
				head = rope[i]
				tail = rope[i + 1]
				
				dx, dy = head[0] - tail[0], head[1] - tail[1]
				if abs(dx) > 1 or abs(dy) > 1:
					tail[0] += 1 if dx > 0 else (0 if dy and not dx else -1)
					tail[1] += 1 if dy > 0 else (0 if dx and not dy else -1)

			visited.add(tuple(rope[-1]))

	print(len(visited))
