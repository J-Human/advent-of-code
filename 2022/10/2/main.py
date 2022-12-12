import os.path
import sys

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	x = 1
	cycle = 1

	crt = ["" for _ in range(6)]
	crt[0] += "#"
	
	for line in file.read().splitlines():		
		for i in range(0, 2 if line.startswith("addx") else 1):
			cycle += 1
			
			if cycle == 241:
				print("\n".join(crt))
				sys.exit(0)

			if i == 1:
				x += int(line.split(" ")[-1])
	
			crt[int((cycle - 1) // 40)] += "#" if ((cycle - 1) % 40) in range(x - 1, x + 2) else "."
