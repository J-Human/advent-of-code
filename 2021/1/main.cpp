#include <deque>
#include <fstream>
#include <iostream>
#include <string>

int main() {
	int data;
	std::ifstream file;

	file.open("2021/1/input.txt");
	if (!file) {
		std::cerr << "Failed to open input file." << std::endl;
		return 1;
	}

	std::deque<int> nums;
	while (file >> data) {
		nums.push_back(data);
	}

	int increases = 0;
	for (std::deque<int>::size_type i = 0; i < nums.size(); ++i) {
		if (i == 0) continue;
		if (nums[i] > nums[i - 1]) {
			increases++;
		}
	}

	std::cout << increases << std::endl;
}
