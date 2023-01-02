import ast
import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	print(sum([len(string) - len(ast.literal_eval(string)) for string in file.read().splitlines()]))
	