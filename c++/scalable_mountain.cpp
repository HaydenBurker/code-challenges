// Write a function that passes in an array of integers representing the height of a mountain at certain intervals and a maximum steepness. It returns true if each number is within the maximum steepness of the next number in either direction and false otherwise

#include <iostream>
#include <vector>

bool is_scalable(std::vector<int> mountain, int maximum_steepness) {
    for (int i = 1; i < mountain.size(); i++) {
        if (abs(mountain[i] - mountain[i - 1]) > maximum_steepness) {
            return false;
        }
    }

    return true;
}

int main() {

    std::cout << is_scalable({1, 2, 3, 4, 5, 4, 3, 2, 1}, 1) << std::endl; // true (1)
    std::cout << is_scalable({4, 6, 7, 4, 2, 6, 3}, 5) << std::endl; // true
    std::cout << is_scalable({2, 5, 9, 7, 3}, 3) << std::endl; // false (0)
    std::cout << is_scalable({42}, 1) << std::endl; // true
    std::cout << is_scalable({5, 3, 6, 12, 10}, 5) << std::endl; // false
    std::cout << is_scalable({12, 4, 2, 1, 1}, 6) << std::endl; // false
    std::cout << is_scalable({3, 3, 3}, 0) << std::endl; // true

    return 0;
}