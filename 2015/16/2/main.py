import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	target = { "children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1 }

	for index, line in enumerate(file.read().splitlines()):
		attributes = { x.split(": ")[0]: int(x.split(": ")[1]) for x in line.replace(":", ",", 1).split(", ")[1:] }

		for k, v in attributes.items():
			if k in ("cats", "trees"):
				if v <= target[k]:
					break
			elif k in ("pomeranians", "goldfish"):
				if v >= target[k]:
					break
			elif target[k] != v:
				break
		else:
			print(index + 1)
			break
