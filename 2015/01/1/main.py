import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	print(sum(1 if direction == "(" else -1 for direction in file.read()))
