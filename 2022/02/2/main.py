import os.path

score = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	matches = file.read().splitlines()
	
	for opponent, _, status in matches:
		shape_value = "ABC".index(opponent) + 1

		if status == "X":
			# Get the index to wrap around later. Shift to the left and add to get the shape value from index.
			score += ((shape_value - 2) % 3) + 1
		elif status == "Y":
			score += 3 + shape_value
		elif status == "Z":
			score += 6 + (shape_value % 3) + 1

print(score)
