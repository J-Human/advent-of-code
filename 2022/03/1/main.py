import os.path
import string

total = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	for bag in file.read().splitlines():
		middle = len(bag) // 2
		compartment_a, compartment_b = map(set, [bag[:middle], bag[middle:]])
		common = (compartment_a & compartment_b).pop()
		
		total += string.ascii_letters.index(common) + 1

print(total)
