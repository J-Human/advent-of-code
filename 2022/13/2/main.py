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
		elif type(right) == int:
			right = [right]
		return cmp(left, right)

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	packets = [eval(packet) for packet in file.read().split("\n") if packet != ""] + [[[2]], [[6]]]
	
	sorted_packets = sorted(packets, key=functools.cmp_to_key(cmp))
	print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
