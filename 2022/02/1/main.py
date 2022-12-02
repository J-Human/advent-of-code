import os.path

score = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	matches = file.read().splitlines()
	
	for match in matches:
		shape_value = ["X", "Y", "Z"].index(match[-1]) + 1
		score += shape_value

		if match in ("C X", "B Z", "A Y"):
			score += 6
		elif ["A", "B", "C"].index(match[0]) + 1 == shape_value:
			score += 3
			
print(score)
