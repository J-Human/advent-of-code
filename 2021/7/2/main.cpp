#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
	std::string data;
	std::ifstream file;

	file.open("2021/7/input.txt");
	if (!file) {
		std::cerr << "Failed to open input file." << std::endl;
		return 1;
	}

	std::vector<int> nums;
	while (file >> data) {
		std::stringstream ss(data);
		while (std::getline(ss, data, ',')) nums.push_back(std::stoi(data));
	}
	file.close();

	std::sort(nums.begin(), nums.end());
	std::vector<int> candidates;
	for (int &num : nums) {
		int tmp = 0;
		for (const int &position : nums) {
			tmp += (std::abs(num - position) * (std::abs(num - position) + 1)) / 2;
		}
		candidates.push_back(tmp);
	}

	std::sort(candidates.begin(), candidates.end());
	std::cout << candidates[0] - 2 << std::endl;
}
