#include <fstream>
#include <iostream>
#include <string>

int main() {
	std::string data;
	std::ifstream file;

	file.open("2021/2/input.txt");
	if (!file) {
		std::cerr << "Failed to open input file." << std::endl;
		return 1;
	}

	int aim = 0, depth = 0, horizontal = 0;
	while (std::getline(file, data)) {
		int amount = data.back() - '0';
		switch (data.front()) {
			case 'd':
				aim += amount;
				break;
			case 'f':
				horizontal += amount;
				depth += aim * amount;
				break;
			case 'u':
				aim -= amount;
				break;
		}
	}
	file.close();

	std::cout << depth * horizontal << std::endl;
}
