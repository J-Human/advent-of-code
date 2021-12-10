#include <fstream>
#include <iostream>
#include <vector>

int main() {
	int data;
	std::ifstream file;

	file.open("2021/01/input.txt");
	if (!file) {
		std::cerr << "Failed to open input file." << std::endl;
		return 1;
	}

	std::vector<int> nums;
	while (file >> data) nums.push_back(data);
	file.close();

	int increases = 0;
	for (std::vector<int>::size_type i = 0; i < nums.size(); ++i) {
		if (i == 0) continue;
		if (nums[i] > nums[i - 1]) increases++;
	}

	std::cout << increases << std::endl;
}
