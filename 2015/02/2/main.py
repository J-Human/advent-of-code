import os.path

total = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	for l, w, h in map(lambda line: map(int, line.split("x")), file.read().splitlines()):
		sides = [l + l + w + w, l + l + h + h, w + w + h + h]
		total += min(sides) + (l * w * h)

print(total)
