import os.path
import re

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	instructions = [list(map(lambda instruction: list(filter(lambda x: x, re.split(r" ?(AND|OR|NOT|LSHIFT|RSHIFT) ", instruction))), instruction.split(" -> "))) for instruction in file.read().splitlines()]
	instructions.remove(list(filter(lambda instruction: instruction[1][0] == "b", instructions))[0])

	wires = { "b": 3176 }
	for instruction in filter(lambda instruction: len(instruction[0]) == 1 and re.match("^[0-9]*$", instruction[0][0]), instructions):
		wires[instruction[1][0]] = int(instruction[0][0])
		instructions.remove(instruction)

	while len(instructions):
		# Not 
		# Bitwise complement of a 16 bit number: (2^16 - 1) - x
		# Range: 0 -> 2^16 - 1
		for wire, value in wires.copy().items():
			references_not = list(filter(lambda instruction: len(instruction[0]) == 2 and instruction[0][1] == wire, instructions))
			for reference in references_not:
				wires[reference[1][0]] = (pow(2, 16) - 1) - wires[reference[0][1]]
				instructions.remove(reference)
				
		# And, Or
		references_two = list(filter(lambda instruction: len(instruction[0]) == 3 and (instruction[0][0] in wires.keys() or re.match("^[0-9]*$", instruction[0][0])) and instruction[0][2] in wires.keys(), instructions))
		for reference in references_two:
			wires[reference[1][0]] = (int(reference[0][0]) if re.match("^[0-9]*$", reference[0][0]) else wires[reference[0][0]]) & wires[reference[0][2]] if reference[0][1] == "AND" else (int(reference[0][0]) if re.match("^[0-9]*$", reference[0][0]) else wires[reference[0][0]]) | wires[reference[0][2]]
			instructions.remove(reference)
			
		# Left shift, Right shift
		references_shift = list(filter(lambda instruction: len(instruction[0]) == 3 and instruction[0][1] in ("LSHIFT", "RSHIFT") and instruction[0][0] in wires.keys(), instructions))
		for reference in references_shift:
			if reference[0][1] == "LSHIFT":
				wires[reference[1][0]] = wires[reference[0][0]] << int(reference[0][2])
			elif reference[0][1] == "RSHIFT":
				wires[reference[1][0]] = wires[reference[0][0]] >> int(reference[0][2])

			instructions.remove(reference)

		wire_to_wire = list(filter(lambda instruction: len(instructions[0][0]) == 1 and instruction[0][0] in wires.keys(), instructions))
		for reference in wire_to_wire:
			wires[reference[1][0]] = wires[reference[0][0]]
			instructions.remove(reference)
			
	print(wires["a"])
		