import os.path

floor = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	for index, direction in enumerate(file.read()):
		floor += 1 if direction == "(" else -1
		if floor == -1:
			print(index + 1)
			break
