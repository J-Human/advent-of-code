import os.path
import re

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	layout, instructions = [part.splitlines() for part in file.read().split("\n\n")]
	stacks = { x: [] for x in range(1, int(layout[-1].strip()[-1]) + 1) }

	for row in layout[:-1]:
		for index, crate in enumerate((" " * 3 + row)[::4][1:]):
			if crate == " ":
				continue

			stacks[index + 1].insert(0, crate)

	for instruction in instructions:
		amount, origin, destination = list(map(int, re.findall("\d+", instruction)))
		
		stacks[destination].extend(reversed(stacks[origin][-amount:]))
		del stacks[origin][-amount:]

	print("".join([stack[-1] for stack in stacks.values()]))
