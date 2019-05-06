// Copyright (c) 2018 kamyu. All rights reserved.

/*
 * Google Code Jam 2018 Round 2 - Problem B. Graceful Chainsaw Jugglers
 * https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/00000000000459f3
 *
 * Time:  O(R^(4/3)*B^(4/3))
 * Space: O(R^(4/3)*B^(4/3))
 *
 */

#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <limits>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::pair;
using std::max;
using std::numeric_limits;

const int MAX_R = 500;
const int MAX_B = 500;

int graceful_chainsaw_jugglers(const vector<vector<float>>& dp) {
    int R, B;
    cin >> R >> B;
    return dp[R][B];
}

int main() {
    vector<vector<float>> dp(MAX_R + 1, vector<float>(MAX_B + 1));
    for (int i = 0; i * (i + 1) / 2 <= MAX_R; ++i) {
        for (int j = 0; j * (j + 1) / 2 <= MAX_B; ++j) {
            if (i == 0 && j == 0) {
                continue;
            }
            if ((j + 1) * i * (i + 1) / 2 > MAX_R ||
                (i + 1) * j * (j + 1) / 2 > MAX_B) {
                break;
            }
            for (int r = MAX_R; r - i >= 0; --r) {
                for (int b = MAX_B; b - j >= 0; --b) {
                    dp[r][b] = max(dp[r][b], 1 + dp[r - i][b - j]);
                }
            }
        }
    }
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": "
             << graceful_chainsaw_jugglers(dp) << endl;
    }
    return 0;
}
