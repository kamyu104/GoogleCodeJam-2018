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

float memoization(const vector<pair<int, int>>& V, int i, int r, int b,
                vector<float> *lookup) {
    if (r < 0 || b < 0) {
        return -numeric_limits<float>::infinity();
    }
    if (i < 0) {
        return 0.0f;
    }
    int key = i * (MAX_R + 1) * (MAX_B + 1) + r * (MAX_B + 1) + b;
    if ((*lookup)[key] == -1) {
        (*lookup)[key] = max(memoization(V, i - 1, r, b, lookup),
                             1 + memoization(V, i - 1,
                                             r - V[i].first, b - V[i].second,
                                             lookup));
    }
    return (*lookup)[key];
}

int graceful_chainsaw_jugglers(const vector<pair<int, int>>& V,
                               vector<float> *lookup) {
    int R, B;
    cin >> R >> B;
    return memoization(V, V.size() - 1, R, B, lookup);
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
    vector<float> lookup((V.size() + 1) * (MAX_R + 1) * (MAX_B + 1), -1);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": "
             << graceful_chainsaw_jugglers(V, &lookup) << endl;
    }
    return 0;
}
