#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
	std::string data;
	std::ifstream file;

	file.open("2021/06/input.txt");
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

	for (int i = 0; i < 80; ++i) {
		std::vector<int> new_nums;

		for (int j = 0; j < nums.size(); ++j) {
			if (nums[j] == 0) {
				nums[j] = 6;
				new_nums.push_back(8);
				continue;
			}
			--nums[j];
		}
		for (int &new_fish : new_nums) nums.push_back(new_fish);
	}

	std::cout << nums.size() << std::endl;
}
