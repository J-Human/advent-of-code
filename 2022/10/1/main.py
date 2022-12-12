import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	x = 1
	total = 0
	cycle = 1
	
	for line in file.read().splitlines():		
		for i in range(0, 2 if line.startswith("addx") else 1):
			cycle += 1

			if i == 1:
				x += int(line.split(" ")[-1])
			
			if cycle in range(20, 221, 40):
				total += x * cycle
		
	print(total)
