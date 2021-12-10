#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
	std::string data;
	std::ifstream file;

	file.open("2021/03/input.txt");
	if (!file) {
		std::cerr << "Failed to open input file." << std::endl;
		return 1;
	}

	std::vector<int> zero(12, 0);
	std::vector<int> one(12, 0);
	while (std::getline(file, data)) {
		for (int i = 0; i < data.size(); ++i) {
			if (data[i] == '0') {
				zero[i]++;
			} else {
				one[i]++;
			}
		}
	}
	file.close();

	std::string gamma = "", epsilon = "";
	for (int i = 0; i < 12; ++i) {
		if (zero[i] > one[i]) {
			gamma += "1";
			epsilon += "0";
		} else {
			gamma += "0";
			epsilon += "1";
		}
	}

	std::cout << std::stoi(gamma, 0, 2) * std::stoi(epsilon, 0, 2) << std::endl;
}
