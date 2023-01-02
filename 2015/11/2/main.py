import os
import re
import string

def increment(text):
	if text[-1] != "z":
		index = string.ascii_lowercase.index(text[-1])
		return text[:-1] + string.ascii_lowercase[index + 1]
		
	return ("a" if len(text) == 1 else increment(text[:-1])) + "a"

def generate(password):
	while True:
		password = increment(password)
		
		if any(combination in password for combination in ["abc", "bcd", "cde", "def", "efg", "fgh", "pqr", "qrs", "rst", "stu", "tuv", "uvw", 'vwx', "wxy", "xyz"]):
			if all(letter not in password for letter in "iol"):
				if len(set(re.findall(r"([a-z])\1", password))) > 1:
					return password
					break

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	password = file.read()
	print(generate(generate(password)))
	