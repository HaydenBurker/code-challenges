// Write a function to replace all instances of character c1 with character c2 and vice versa

#include <iostream>

std::string double_character_swap(std::string str, char c1, char c2) {
    for (char& c : str) {
        if (c == c1) c = c2;
        else if (c == c2) c = c1;
    }
    return str;
}

int main() {
    std::cout << double_character_swap("Hello world!", 'l', 'o') << '\n'; // "Heool wlrod"
    std::cout << double_character_swap("12543", '3', '5') << '\n'; // "12345"
    std::cout << double_character_swap("No change", 'o', 'o') << '\n'; // "No change"
    std::cout << double_character_swap("No change", '!', '0') << '\n'; // "No change"
    std::cout << double_character_swap("", 'a', 'b') << '\n'; // ""

    return 0;
}