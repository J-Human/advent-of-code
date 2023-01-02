import itertools
import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	distances = {}
	towns = set()
	
	for a, b, distance in [(line.split(" ")[0], line.split(" ")[2], int(line.split(" ")[-1])) for line in file.read().splitlines()]:
		distances[(a, b)] = distance
		distances[(b, a)] = distance
		towns.update([a, b])
	
	lengths = []
	for route in itertools.permutations(towns):
		lengths.append(sum(distances[(route[town], route[town + 1])] for town in range(len(route) - 1)))
	
	print(max(lengths))
