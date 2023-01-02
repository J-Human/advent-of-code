import os.path

santa_coordinates_history = set([(0, 0)])
robosanta_coordinates_history = set([(0, 0)])
santa_coordinates = [0, 0]
robosanta_coordinates = [0, 0]

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	for index, direction in enumerate(file.read()):
		in_charge_coordinates = santa_coordinates if (index + 1) % 2 else robosanta_coordinates
		in_charge_coordinates_history = santa_coordinates_history if (index + 1) % 2 else robosanta_coordinates_history
		
		in_charge_coordinates[0] += 1 if direction == ">" else (-1 if direction == "<" else 0)
		in_charge_coordinates[1] += 1 if direction == "^" else (-1 if direction == "v" else 0)
		
		in_charge_coordinates_history.add(tuple(in_charge_coordinates[:]))

print(len(santa_coordinates_history | robosanta_coordinates_history))
