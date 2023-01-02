import os.path
import re

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	string = file.read()
	
	for _ in range(40):
		matches = [match[0] for match in re.findall(r'((\d)\2*)', string)]
		new_string = []
		for match in matches:
			new_string.append(str(len(match)) + match[0])
			
		string = "".join(new_string)
	
	print(len(string))
