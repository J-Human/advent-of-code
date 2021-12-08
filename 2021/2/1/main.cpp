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

	int depth = 0, horizontal = 0;
	while (std::getline(file, data)) {
		int distance = data.back() - '0';
		switch (data.front()) {
			case 'd':
				depth += distance;
				break;
			case 'f':
				horizontal += distance;
				break;
			case 'u':
				depth -= distance;
				break;
		}
	}
	file.close();

	std::cout << depth * horizontal << std::endl;
}
