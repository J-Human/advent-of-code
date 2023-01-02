import os.path
import re

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	print(sum(map(int, re.findall("-?\d+", file.read()))))
