// Write a function that returns the elements in an array that are strictly greater than their adjacent neighbors

#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

std::vector<int> mini_peaks(std::vector<int> nums) {
    std::vector<int> peaks;

    for (int i = 1; i < (nums.size() > 0 ? nums.size() - 1 : 0); i++) {
        if (nums[i] > nums[i-1] && nums[i] > nums[i+1]) peaks.push_back(nums[i]);
    }
    
    return peaks;
}

std::ostream& operator<<(std::ostream& os, std::vector<int>&& v) {
    os << "[";
    if (!v.empty()) {
        std::copy(v.begin(), v.end(), std::ostream_iterator<int>(os, ", "));
        os << "\b\b";
    }
    os << "]";
    return os;
}

int main() {
    std::cout << mini_peaks({1, 2, 3}) << '\n'; // []
    std::cout << mini_peaks({3, 2, 1}) << '\n'; // []
    std::cout << mini_peaks({1, 3, 2}) << '\n'; // [3]
    std::cout << mini_peaks({2, 1, 5, 6, 7, 3, 2, 5, 3, 6, 1, 3}) << '\n'; // [7, 5, 6]
    std::cout << mini_peaks({1, 2, 2, 1, 2, 3, 1}) << '\n'; // [3]
    std::cout << mini_peaks({}) << '\n'; // []

    return 0;
}