// Write a function that takes in an array of the number pins knocked down by each ball and calculates the bowling score

#include <iostream>
#include <vector>

int bowling_score(std::vector<int> scorecard) {
    int score = 0, card_idx = 0;

    for(int i = 1; i <= 10; i++) {
        int first = scorecard[card_idx++];
        if (first == 10) {
            score += first + scorecard[card_idx] + scorecard[card_idx + 1];
            continue;
        }

        int second = scorecard[card_idx++];
        if (first + second == 10) score += scorecard[card_idx];

        score += first + second;
    }

    return score;
}

int main() {
    std::cout << bowling_score({10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}) << '\n'; // 300
    std::cout << bowling_score({0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}) << '\n'; // 0
    std::cout << bowling_score({5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5}) << '\n'; // 150
    std::cout << bowling_score({10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10, 5, 5, 10}) << '\n'; // 200
    std::cout << bowling_score({3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 8, 1, 7, 2, 6, 3, 5, 3, 0, 8}) << '\n'; // 80
    std::cout << bowling_score({10, 10, 7, 3, 9, 1, 7, 2, 8, 0, 8, 2, 10, 10, 6, 3}) << '\n'; // 174
    std::cout << bowling_score({10, 10, 10, 8, 2, 9, 1, 7, 1, 10, 0, 10, 2, 7, 10, 10, 5}) << '\n'; // 188

    return 0;
}