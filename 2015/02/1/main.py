import os.path

total = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	for l, w, h in map(lambda line: map(int, line.split("x")), file.read().splitlines()):
		sides = [2 * l * w, 2 * w * h, 2 * h * l]
		total += (min(sides) / 2) + sum(sides)

print(total)
