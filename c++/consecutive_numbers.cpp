// Write a function that determines whether an array of integers can be rearranged to form a consecutive list of numbers

#include <iostream>
#include <vector>
#include <iterator>

bool consecutive_numbers(std::vector<int> nums) {
    std::sort(nums.begin(), nums.end());

    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] != nums[i - 1] + 1) return false;
    }

    return true;
}

int main() {
    std::cout << consecutive_numbers({1,4,5,3,2}) << '\n'; // true
    std::cout << consecutive_numbers({4,5,1,7,2}) << '\n'; // false
    std::cout << consecutive_numbers({-3,-2,-1,0,1}) << '\n'; // true
    std::cout << consecutive_numbers({6,3,5,6,4,2}) << '\n'; // false
    std::cout << consecutive_numbers({5,3}) << '\n'; // false
    std::cout << consecutive_numbers({6,2,5,7,3,1,4,0}) << '\n'; // true

    return 0;
}