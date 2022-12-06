import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:	
	buffer = file.read()
	
	for i in range(0, len(buffer) + 1):
		if len(set(buffer[i:i + 14])) == 14:
			print(i + 14)
			break
