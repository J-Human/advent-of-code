import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	print(sum([(len('"' + string.replace("\\", "\\\\").replace('"', '\\"') + '""') - 1) - len(string) for string in file.read().splitlines()]))
