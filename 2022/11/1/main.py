import math
import os.path
import re

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	monkeys = []
	cycle = 0
	
	for monkey in file.read().split("\n\n"):
		details = re.sub(r".*: ?", "", monkey, flags=re.MULTILINE)
		details = details.replace("divisible by ", "").replace("throw to monkey ", "").replace("new = ", "")
		worry_levels, operation, test, if_true, if_false = details.strip().split("\n")
	
		monkeys.append({ 
			"worry_levels": list(map(int, worry_levels.split(", "))),
			"operation": operation,
			"test": int(test), 
			"if_true": int(if_true),
			"if_false": int(if_false),
			"amount": 0 
		})

	while cycle < 20:
		for monkey in monkeys:
			for index in range(0, len(monkey["worry_levels"])):
				worry_level = monkey["worry_levels"].pop()
				new_worry_level = int(eval(monkey["operation"], { "old": worry_level }) // 3)
				monkey["amount"] += 1
				
				divisible = new_worry_level % monkey["test"] == 0
				monkeys[monkey["if_true" if divisible else "if_false"]]["worry_levels"].append(new_worry_level)
				
		cycle += 1
		
	print(math.prod(sorted([monkey["amount"] for monkey in monkeys])[-2:]))
			