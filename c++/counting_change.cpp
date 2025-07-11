// Write a function that takes in an array representing change (quarters, dimes, nickels, pennies) and the price of an item
// Return true if there is enough change to cover the price of the item and false otherwize

#include <iostream>
#include <vector>

bool has_enough_change(std::vector<int> change, double price) {
    return (change[0] * 25 + change[1] * 10 + change[2] * 5 + change[3]) >= (price * 100);
}

int main() {
    std::cout << "Hello world!" << std::endl;

    std::cout << has_enough_change({0, 0, 20, 5}, 0.75) << std::endl; // true
	std::cout << has_enough_change({30, 40, 20, 5}, 12.55) << std::endl; // true
	std::cout << has_enough_change({1, 0, 2555, 219}, 127.75) << std::endl; // true
	std::cout << has_enough_change({1, 335, 0, 219}, 35.21) << std::endl; // true
	std::cout << has_enough_change({2, 100, 0, 0}, 14.11) << std::endl; // false
	std::cout << has_enough_change({10, 0, 0, 50}, 13.85) << std::endl; // false
	std::cout << has_enough_change({1, 0, 5, 219}, 19.99) << std::endl; // false

    return 0;
}