import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	print(max([sum(map(int, calories.split("\n"))) for calories in file.read().split("\n\n")]))