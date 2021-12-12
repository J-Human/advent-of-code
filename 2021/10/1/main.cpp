#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

int main() {
	std::string data;
	std::ifstream file;

	file.open("2021/10/input.txt");
	if (!file) {
		std::cerr << "Failed to open input file." << std::endl;
		return 1;
	}

	std::vector<std::string> lines;
	while (std::getline(file, data)) lines.push_back(data);
	file.close();

	std::map<char, char> grouping_symbols = {{'(', ')'}, {'{', '}'}, {'[', ']'}, {'<', '>'}};
	std::map<char, int> points_per_symbol = {{')', 3}, {'}', 1197}, {']', 57}, {'>', 25137}};

	int total_points = 0;
	for (std::string &line : lines) {
		std::vector<char> chars;
		for (char character : line) {
			if (grouping_symbols.count(character) > 0) {
				chars.push_back(character);
				continue;
			} else if (character != grouping_symbols[chars.back()]) {
				total_points += points_per_symbol[character];
				break;
			}
			chars.pop_back();
		}
	}

	std::cout << total_points << std::endl;
}
