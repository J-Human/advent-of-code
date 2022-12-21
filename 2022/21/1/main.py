import os.path
import re

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	instructions = [instruction.split(": ") for instruction in file.read().splitlines()]
	monkeys = {}
	
	while instructions:
		for monkey, expression in instructions:
			if re.match("\d+", expression):
				monkeys[monkey] = int(expression)
				instructions.remove([monkey, expression])
			else:
				first, _, second = expression.split(" ")
				if monkeys.get(first, None) and monkeys.get(second, None):
					monkeys[monkey] = eval(expression, monkeys)
					instructions.remove([monkey, expression])
	
	print(monkeys["root"])
