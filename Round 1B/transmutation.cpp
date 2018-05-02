// Copyright (c) 2018 kamyu. All rights reserved.

/*
 * Google Code Jam 2018 Round 1B - Problem C. Transmutation
 * https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard/000000000003675c
 *
 * Time  : O(M^3 * logS)
 * Space : O(M^2)
 *
 */

#include <iostream>
#include <vector>
#include <numeric>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::accumulate;

int find_debt(const vector<int64_t>& G) {
    for (int i = 0; i < G.size(); ++i) {
        if (G[i] < 0LL) {
            return i;
        }
    }
    return G.size();
}

vector<int64_t> multiply(vector<int64_t> R, int64_t k) {
    for (auto& g : R) {
        g *= k;
    }
    return R;
}

void add(vector<int64_t> *R1, const vector<int64_t>& R2) {
    for (int i = 0; i < R1->size(); ++i) {
        (*R1)[i] += R2[i];
    }
}

bool impossible(int64_t L, vector<vector<int64_t>> R, vector<int64_t> G) {
    G[0] -= L;
    if (G[0] >= 0LL) {
        return false;
    }
    for (int i = 0; i != G.size(); i = find_debt(G)) {
        if (R[i][i] != 0LL ||
            accumulate(G.cbegin(), G.cend(), G[i]) < 0) {  // critical purning
            return true;
        }
        add(&G, multiply(R[i], G[i])), G[i] = 0;
        auto& Ri = R[i];
        for (auto& Rj : R) {
            if (!Rj.empty() && Rj[i] != 0LL) {
                add(&Rj, multiply(Ri, Rj[i])), Rj[i] = 0;
            }
        }
        Ri.clear();
    }
    return false;
}

int64_t transmutation() {
    int M;
    cin >> M;
    vector<vector<int64_t>> R(M, vector<int64_t>(M, 0LL));
    for (int i = 0; i < M; ++i) {
        int R1, R2;
        cin >> R1 >> R2;
        R[i][R1 - 1] = R[i][R2 - 1] = 1;
    }
    vector<int64_t> G(M, 0LL);
    for (int i = 0; i < M; ++i) {
        cin >> G[i];
    }
    auto left = G[0];
    auto right = accumulate(G.cbegin(), G.cend(), static_cast<int64_t>(0LL));
    while (left <= right) {
        const auto mid = left + (right - left) / 2;
        if (impossible(mid, R, G)) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return left - 1;
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": " << transmutation() << endl;
    }
    return 0;
}
