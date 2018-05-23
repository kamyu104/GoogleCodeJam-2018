// Copyright (c) 2018 kamyu. All rights reserved.

/*
 * Google Code Jam 2018 Round 2 - Problem B. Graceful Chainsaw Jugglers
 * https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard/00000000000459f3
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
    vector<pair<int, int>> V;
    for (int i = 0; i <= MAX_R; ++i) {
        for (int j = 0; j <= MAX_B; ++j) {
            if (i == 0 && j == 0) {
                continue;
            }
            if ((j + 1) * i * (i + 1) / 2 <= MAX_R &&
                (i + 1) * j * (j + 1) / 2 <= MAX_B) {
                V.emplace_back(i, j);
            }
        }
    }
    vector<vector<float>> dp(MAX_R + 1, vector<float>(MAX_B + 1));
    for (int i = 0; i < V.size(); ++i) {
        for (int r = MAX_R; r - V[i].first >= 0; --r) {
            for (int b = MAX_B; b - V[i].second >= 0; --b) {
                dp[r][b] = max(dp[r][b], 1 + dp[r - V[i].first][b - V[i].second]);
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
