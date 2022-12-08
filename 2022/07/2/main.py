import collections
import os.path
import re
	
with open(os.path.dirname(__file__) + "/../input.txt") as file:
	cwd = []
	fs = collections.defaultdict(int)

	for line in file.read().splitlines():
		if line[0] == "$":
			full_command = line.split(" ")[1:]

			if full_command[0] == "cd":
				destination = full_command[1]

				if destination == "..":
					cwd.pop()
				elif destination == "/":
					cwd = ["/"]
				else:
					cwd.append(destination + "/")
		elif re.match("\d+", line[0]):
			parent_cwd = cwd[:]
			while len(parent_cwd):
				fs["".join(parent_cwd)] += int(line.split(" ")[0])
				parent_cwd.pop()

	print(sorted([n for n in fs.values() if (7e7 - fs["/"]) + n >= 3e7])[0])
