#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "../../../vendor/strutil.h"

int main() {
	std::string data;
	std::ifstream file;

	file.open("2021/08/input.txt");
	if (!file) {
		std::cerr << "Failed to open input file." << std::endl;
		return 1;
	}

	int count = 0;
	while (std::getline(file, data)) {
		std::vector<std::string> sides = strutil::split(data, " | ");
		std::vector<std::string> chars = strutil::split(sides.back(), " ");
		for (const std::string &v : chars)
			if (v.size() <= 4 || v.size() == 7) count++;
	}
	file.close();

	std::cout << count << std::endl;
}
