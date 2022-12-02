import os.path

score = 0

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	matches = file.read().splitlines()
	
	partners = { "A": { "win": 2, "lose": 3 }, "B": { "win": 3, "lose": 1 }, "C": { "win": 1, "lose": 2 } }
	
	for opponent, _, status in matches:
		if status == "Y":
			score += 3 + (["A", "B", "C"].index(opponent) + 1)
		elif status == "X":
			score += partners[opponent]["lose"]	
		elif status == "Z":
			score += 6 + partners[opponent]["win"]

print(score)
