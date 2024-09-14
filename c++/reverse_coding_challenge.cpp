// Create a function that produces the following outputs when fed in the following inputs
// 751 -> 594, 3 -> 0, 64 -> 18, 67666 -> 999, 8877 -> 1089, 12345 -> 0, 54321 -> 41976

#include <iostream>

int solution(int num) {
    std::string num_str = std::to_string(num);
    std::sort(num_str.begin(), num_str.end());
    return std::max(0, num - std::stoi(num_str));
}

int main() {
    std::cout << solution(751) << '\n'; // 594
    std::cout << solution(3) << '\n'; // 0
    std::cout << solution(64) << '\n'; // 18
    std::cout << solution(67666) << '\n'; // 999
    std::cout << solution(8877) << '\n'; // 1089
    std::cout << solution(12345) << '\n'; // 0
    std::cout << solution(54321) << '\n'; // 41976

    return 0;
}