import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:	
	buffer = file.read()

	for i in range(0, len(buffer) - 3):
		if len(set(buffer[i:i + 4])) == 4:
			print(i + 4)
			break
