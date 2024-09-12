// Write a function that checks if a string is a valid hex code

#include <iostream>

bool is_valid_hex_code(std::string str) {
    if (str.length() != 7) return false;
    if (str[0] != '#') return false;
    
    for (const char& c : str.substr(1)) {
        if (c >= '0' && c <= '9') continue;
        if (tolower(c) >= 'a' && tolower(c) <= 'f') continue;
        return false;
    }

    return true;
}

int main() {
    std::cout << is_valid_hex_code("#000000") << '\n'; // true (1)
    std::cout << is_valid_hex_code("#ffffff") << '\n'; // true
    std::cout << is_valid_hex_code("123456") << '\n'; // false (0)
    std::cout << is_valid_hex_code("#abcdef") << '\n'; // true
    std::cout << is_valid_hex_code("#bcdefg") << '\n'; // false
    std::cout << is_valid_hex_code("") << '\n'; // false
    std::cout << is_valid_hex_code("#12345") << '\n'; // false
    std::cout << is_valid_hex_code("#1Cd9fA") << '\n'; // true
    std::cout << is_valid_hex_code("15463#c") << '\n'; // false
    std::cout << is_valid_hex_code("#146c8a3") << '\n'; // false

    return 0;
}