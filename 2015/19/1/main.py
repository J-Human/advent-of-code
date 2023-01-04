import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	possible = set()
	replacements, start = file.read().split("\n\n")
	replacements = [(line.split(" ")[0], line.split(" ")[-1]) for line in replacements.split("\n")]
	
	for a, b in replacements:
		indices = [i for i in range(len(start)) if start.startswith(a, i)]
		
		for i, index in enumerate(indices):
			possible.add(start[:index] + b + start[index + len(a):])
	
	print(len(possible))
