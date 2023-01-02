import os.path
import re

count = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	lines = file.read().splitlines()
	for line in lines:
		for pattern in [r".*([a-z]{2})([a-z]*)?\1", r".*([a-z])[a-z](?=\1).*"]:
			if not re.match(pattern, line):
				break
		else:
			count += 1

print(count)
