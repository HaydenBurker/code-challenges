// Write a function that finds the odd integer in an array
// The array will always have one

#include <iostream>
#include <vector>
#include <unordered_set>

int odd_integer(std::vector<int> nums) {
    std::unordered_set<int> odd_nums = {};

    for (const int& num : nums) {
        if (odd_nums.find(num) == odd_nums.end()) odd_nums.insert(num);
        else odd_nums.erase(num);
    }

    return *odd_nums.begin();
}

int main() {
    std::cout << odd_integer({1}) << '\n'; // 1
    std::cout << odd_integer({5, 3, 7, 4, 4, 3, 7, 4, 5, 7, 4}) << '\n'; // 7
    std::cout << odd_integer({1, 2, 3, 4, 5, 4, 3, 2, 1}) << '\n'; // 5
    std::cout << odd_integer({-5, 3, -1, -2, 3, -1, 1, -5, 1, -2, -1}) << '\n'; // -1

    return 0;
}