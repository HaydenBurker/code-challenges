// Write a function that takes an array of integers and returns true if there are more odd integers than even integers and false otherwize
#include <iostream>
#include <vector>

bool odd_over_even(std::vector<int> ints) {
    int odd = 0, even = 0;

    for (const int number : ints) {
        if (number % 2 == 0) ++even;
        else ++odd;
    }

    return odd > even;
}

int main() {
    std::cout << odd_over_even({1}) << std::endl; // true
    std::cout << odd_over_even({2}) << std::endl; // false
    std::cout << odd_over_even({1, 2, 3}) << std::endl; // true
    std::cout << odd_over_even({1, 2, 3, 4, 6}) << std::endl; // false
    std::cout << odd_over_even({}) << std::endl; // false
    std::cout << odd_over_even({5, 10, 2, 3, 2345, 97, 42}) << std::endl; // true

    return 0;
}