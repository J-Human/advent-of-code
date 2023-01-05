import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	target = set([("children", 3), ("cats", 7), ("samoyeds", 2), ("pomeranians", 3), ("akitas", 0), ("vizslas", 0), ("goldfish", 5), ("trees", 3), ("cars", 2), ("perfumes", 1)])
	
	for index, line in enumerate(file.read().splitlines()):
		attributes = set([(v.split(": ")[0], int(v.split(": ")[1])) for v in line.replace(":", ",", 1).split(", ")[1:]])

		if len(target & attributes) >= len(attributes):
			print(index + 1)
			break
