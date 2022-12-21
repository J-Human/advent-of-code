import os.path
import re

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	instructions = [instruction.split(": ") for instruction in file.read().splitlines()]
	monkeys = {}

	humn = [instruction for instruction in instructions if instruction[0] == "humn"][0]
	instructions.remove(humn)
	instructions.append(["humn", 1j])

	root = [instruction for instruction in instructions if instruction[0] == "root"][0]
	root_first, _, root_second = root[1].split(" ")
	instructions.remove(root)
	
	while instructions:
		for monkey, expression in instructions:
			if type(expression) == complex or re.match("\d+", expression):
				monkeys[monkey] = int(expression) if type(expression) != complex else expression
				instructions.remove([monkey, expression])
			else:
				first, _, second = expression.split(" ")
				if monkeys.get(first, None) and monkeys.get(second, None):
					monkeys[monkey] = eval(expression, monkeys)
					instructions.remove([monkey, expression])

	print((monkeys[root_second].real - monkeys[root_first].real) // monkeys[root_first].imag)
