import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	instructions = file.read().splitlines()
	registers = { "a": 1, "b": 0 }
	i = 0
	
	while i < len(instructions):
		line = instructions[i]
		
		if line.startswith("hlf"):
			_, register = line.split(" ")
			registers[register] = registers[register] / 2
		elif line.startswith("tpl"):
			_, register = line.split(" ")
			registers[register] = registers[register] * 3
		elif line.startswith("inc"):
			_, register = line.split(" ")
			registers[register] = registers[register] + 1
		elif line.startswith("jmp"):
			i += eval(line.split(" ")[1])
			continue
		elif line.startswith("jio"):
			register = line.split(", ")[0][-1]
			
			if registers[register] == 1:
				i += eval(line.split(", ")[1])
				continue
		elif line.startswith("jie"):
			register = line.split(", ")[0][-1]
			
			if registers[register] % 2 == 0:
				i += eval(line.split(", ")[1])
				continue
		
		i += 1
	
	print(registers["b"])
