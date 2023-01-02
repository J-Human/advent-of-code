import os.path

def get_sum(data):
	if type(data) == int:
		return data
	elif type(data) == list:
		return sum(map(get_sum, data))
	elif type(data) == dict:
		return 0 if "red" in data.values() else sum(map(get_sum, data.values()))
	
	return 0
	
with open(os.path.dirname(__file__) + "/../input.txt") as file:
	print(get_sum(eval(file.read())))
