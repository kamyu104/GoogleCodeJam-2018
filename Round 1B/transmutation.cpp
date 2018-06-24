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
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::accumulate;
using std::min_element;
using std::distance;
using std::find;

int find_debt(const vector<double>& G) {
    auto debt = *min_element(G.cbegin(), G.cend());
    return debt >= 0.0 ?
        G.size() : distance(G.cbegin(), find(G.cbegin(), G.cend(), debt));
}

vector<double> multiply(vector<double> R, double k) {
    for (auto& g : R) {
        g *= k;
    }
    return R;
}

void add(vector<double> *R1, const vector<double>& R2) {
    for (int i = 0; i < R2.size(); ++i) {
        (*R1)[i] += R2[i];
    }
}

bool impossible(double L, vector<vector<double>> R, vector<double> G) {
    G[0] -= L;
    if (G[0] >= 0.0) {
        return false;
    }
    for (int i = 0; i != G.size(); i = find_debt(G)) {
        auto& Ri = R[i];
        // any element in G or R is possible from -10^22 ~ 10^22,
        // Using double instead of int64_t,
        // it never overflows in the largest test set.
        // (double gives 15 significant decimal digits precision)
        if (Ri[i] != 0.0) {
            return true;
        }
        add(&G, multiply(Ri, G[i])), G[i] = 0.0;
        for (auto& Rj : R) {
            if (!Rj.empty() && Rj[i] != 0.0) {
                add(&Rj, multiply(Ri, Rj[i])), Rj[i] = 0.0;
            }
        }
        Ri.clear();
    }
    return false;
}

int64_t transmutation() {
    int M;
    cin >> M;
    vector<vector<double>> R(M, vector<double>(M, 0.0));
    for (int i = 0; i < M; ++i) {
        int R1, R2;
        cin >> R1 >> R2;
        R[i][R1 - 1] = R[i][R2 - 1] = 1;
    }
    vector<double> G(M, 0.0);
    for (int i = 0; i < M; ++i) {
        cin >> G[i];
    }
    int64_t left = G[0];
    int64_t right = accumulate(G.cbegin(), G.cend(), 0.0);
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
