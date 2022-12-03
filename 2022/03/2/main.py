import functools
import os.path
import string

total = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	bags = file.read().splitlines()
	
	for group in [map(set, bags[i:i + 3]) for i in range(0, len(bags), 3)]:
		common = functools.reduce(lambda x, y: x & y, group).pop()
		total += string.ascii_letters.index(common) + 1

print(total)
