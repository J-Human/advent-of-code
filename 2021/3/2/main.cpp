#include <deque>
#include <fstream>
#include <iostream>

int get_rate(const std::deque<std::string> &binaries, const std::string &type) {
	std::deque<std::string> matches(binaries);
	std::deque<std::string> ones, zeros;
	int current = 0;

	while (matches.size() >= 2) {
		for (std::string &binary : matches) (binary[current] == '0' ? zeros : ones).push_back(binary);
		(type == "oxygen" ? ones.size() < zeros.size() : ones.size() >= zeros.size()) ? matches.swap(ones) : matches.swap(zeros);

		zeros.clear();
		ones.clear();
		current++;
	}

	return std::stoi(matches.front(), 0, 2);
}

int main() {
	std::string data;
	std::ifstream file;

	file.open("2021/3/input.txt");
	if (!file) {
		std::cerr << "Failed to open input file." << std::endl;
		return 1;
	}

	std::deque<std::string> nums;
	while (std::getline(file, data)) {
		nums.push_back(data);
	}
	file.close();
	
	std::cout << get_rate(nums, "oxygen") * get_rate(nums, "co2") << std::endl;
}
