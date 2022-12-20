import os.path

with open(os.path.dirname(__file__) + "/../input.txt") as file:
	nums = [[index, int(num)] for index, num in enumerate(file.read().splitlines())]
	
	for index in range(0, len(nums)):
		num_index = [i for i, v in enumerate(nums) if v[0] == index][0]
		nums.insert((nums[num_index][1] + num_index) % (len(nums) - 1), nums.pop(num_index))
		
	zero_index = [i for i, v in enumerate(nums) if not v[1]][0]
	print(sum([nums[(zero_index + x) % len(nums)][1] for x in (1000, 2000, 3000)]))
