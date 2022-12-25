import math
import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	decimal_total = 0

	for snafu_num in file.read().splitlines():
		for index, digit in enumerate(snafu_num, start=-(len(snafu_num) - 1)):
			decimal_total += math.floor(5 ** abs(index)) * (int(digit) if digit not in ("-", "=") else (-1 if digit == "-" else -2))

	snafu_total = ""
	while decimal_total:
		quotient, remainder = divmod(decimal_total, 5)
		snafu_total += "012=-"[remainder]
		decimal_total = quotient + (remainder > 2)

	print(snafu_total[::-1])
