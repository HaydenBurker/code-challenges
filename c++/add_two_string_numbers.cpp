// Write a function that adds two non-negative numbers that are strings
// Empty strings are treated as "0"
// Strings with non-numerical characters are treated as "-1"

#include <iostream>
#include <algorithm>
#include <sstream>

bool is_string_num(std::string& str) {
    return std::all_of(str.begin(), str.end(), [](char& c){ return c >= '0' && c <= '9'; });
}

void trim_zeros(std::string& str) {
    int i = 0;
    while (str[i] == '0') i++;
    if (i > 0) str.erase(0, i);
    if (str.empty()) str = "0";
}

std::string add_string_nums(std::string str1, std::string str2) {
    if (!is_string_num(str1) || !is_string_num(str2)) return "-1";

    trim_zeros(str1);
    trim_zeros(str2);

    if (str1.length() < str2.length()) str1.insert(0, str2.length() - str1.length(), '0');
    else if (str1.length() > str2.length()) str2.insert(0, str1.length() - str2.length(), '0');

    std::stringstream ss;
    bool carry = false;

    for (int i = str1.length() - 1; i >= 0; i--) {
        int result = int(str1[i] - '0') + int(str2[i] - '0') + int(carry);
        carry = bool(result / 10);
        ss << result % 10;
    }

    if (carry) ss << '1';

    std::string added_str = ss.str();
    std::reverse(added_str.begin(), added_str.end());

    return added_str;
}

int main() {
    std::cout << add_string_nums("1", "2") << '\n'; // "3"
    std::cout << add_string_nums("abc", "123") << '\n'; // "-1"
    std::cout << add_string_nums("", "") << '\n'; // "0"
    std::cout << add_string_nums("00004", "16") << '\n'; // "20"
    std::cout << add_string_nums("999999", "1") << '\n'; // "1000000"
    std::cout << add_string_nums("1", "999999") << '\n'; // "1000000"
    std::cout << add_string_nums("987654321", "987654321") << '\n'; // "1975308642"
    std::cout << add_string_nums("40611824854803826359486701167003356192452960279353826740353279356972345798375769983", "2965740275") << '\n'; // "40611824854803826359486701167003356192452960279353826740353279356972345801341510258"

    return 0;
}