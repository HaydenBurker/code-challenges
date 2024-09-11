// Write a function that makes a box based on size n

#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

std::string make_line(char c, int length) {
    std::string line = "";

    for (int i = 0; i < length; i++) line += c;

    return line;
}

std::vector<std::string> make_box(int size) {
    std::vector<std::string> box = {};

    box.push_back(make_line('#', size));
    for (int i = 1; i < size - 1; i++) {
        box.push_back("#" + make_line(' ', size - 2) + "#");
    }
    if (size > 1) box.push_back(make_line('#', size));

    return box;
}

std::ostream& operator<< (std::ostream& os, std::vector<std::string>&& v) {
    std::copy(v.begin(), v.end(), std::ostream_iterator<std::string>(os, "\n"));
    return os;
}

int main() {
    for (int i = 1; i <= 10; i++) std::cout << make_box(i) << '\n';
    return 0;
}