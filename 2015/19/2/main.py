import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	replacements, start = file.read().split("\n\n")
	replacements = [(line.split(" ")[0], line.split(" ")[-1]) for line in replacements.split("\n")]

	total = 0
	originals = replacements.copy()
	
	while start != "e":
		replacements = replacements or originals.copy()
		replacement = max(replacements, key=lambda conversion: len(conversion[1]))

		new = start.replace(replacement[1], replacement[0], 1)
		if start != new:
			total += 1
		else:
			replacements.remove(replacement)
		
		start = new
	
	print(total)
