import os.path

coordinates_history = set([(0, 0)])
coordinates = [0, 0]

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	for direction in file.read():
		coordinates[0] += 1 if direction == ">" else (-1 if direction == "<" else 0)
		coordinates[1] += 1 if direction == "^" else (-1 if direction == "v" else 0)
		
		coordinates_history.add(tuple(coordinates[:]))
        
print(len(coordinates_history))
