import functools
import os.path

def cmp(left, right):
	if type(left) == int and type(right) == int:
		return -1 if left < right else left > right

	elif type(left) == list and type(right) == list:
		for a, b in zip(left, right):
			if cmp(a, b):
				return cmp(a, b)			

		return cmp(len(left), len(right))
	else:
		if type(left) == int:
			left = [left]
		elif type (right) == int:
			right = [right]
		return cmp(left, right)
			

total = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	pairs = [[eval(packet) for packet in pair.splitlines()] for pair in file.read().split("\n\n")]

	for index, pair in enumerate(pairs):
		if pair == sorted(pair, key=functools.cmp_to_key(cmp)):
			total += index + 1

print(total)
