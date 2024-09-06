#include <iostream>
#include <utility>


std::pair<int, int> xor_swap(int a, int b) {
    a = a ^ b; // 0 0 -> 0 | 0 1 -> 1 | 1 0 -> 1 | 1 1 -> 0
    b = a ^ b; // 0 0 -> 0 | 1 1 -> 0 | 1 0 -> 1 | 0 1 -> 1
    a = a ^ b; // 0 0 -> 0 | 1 0 -> 1 | 1 1 -> 0 | 0 1 -> 1
    return std::make_pair(a, b);
}

std::string pair_to_string(std::pair<int, int> result) {
    return "(" + std::to_string(result.first) + ", " + std::to_string(result.second) + ")";
}

int main() {
    std::cout << pair_to_string(xor_swap(1, 2)) << '\n'; // (2, 1)
    std::cout << pair_to_string(xor_swap(1, 1)) << '\n'; // (1, 1)
    std::cout << pair_to_string(xor_swap(5, 3)) << '\n'; // (3, 5)
    std::cout << pair_to_string(xor_swap(3, 5)) << '\n'; // (5, 3)
    std::cout << pair_to_string(xor_swap(12345, 54321)) << '\n'; // (54321, 12345)
    std::cout << pair_to_string(xor_swap(4343, 3434)) << '\n'; // (3434, 4343) 
    return 0;
}