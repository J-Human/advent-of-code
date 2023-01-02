import hashlib
import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	number = 1
	secret_key = file.read()
	
	while True:
		if hashlib.md5(f"{secret_key}{number}".encode("utf-8")).hexdigest().startswith("0" * 6):
			print(number)
			break
		else:
			number += 1
