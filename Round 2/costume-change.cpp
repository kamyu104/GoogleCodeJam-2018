// Copyright (c) 2018 kamyu. All rights reserved.

/*
 * Google Code Jam 2018 Round 2 - Problem C. Costume Change
 * https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard/0000000000045875
 *
 * Time:  O(N^3 * sqrt(N))
 * Space: O(N)
 *
 */

#include <iostream>
#include <vector>
#include <queue>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::queue;

bool dfs(const vector<vector<int>>& edge,
         int u,
         const vector<int>& level,
         vector<bool> *vis,
         vector<int> *pair1,
         vector<int> *pair2) {
    (*vis)[u] = true;
    for (auto it = edge[u].begin(); it != edge[u].end(); ++it) {
        int v = (*pair2)[*it];
        if (v == -1 || (!(*vis)[v] && level[u] < level[v] &&
                        dfs(edge, v, level, vis, pair1, pair2))) {
            (*pair1)[u] = *it, (*pair2)[*it] = u;
            return true;
       }
    }
    return false;
}

int hopcroftKarp(const vector<vector<int>>& edge) {
    const int n = edge.size();  // n is the number of left nodes
    vector<bool> vis(n);
    vector<int> level(n);
    vector<int> pair1(n, -1);
    vector<int> pair2(n, -1);
    for (int match = 0; ;) {
        queue<int> Q;
        for (int i = 0; i < n; ++i) {
            if (pair1[i] == -1) {
                level[i] = 0;
                Q.emplace(i);
            } else {
                level[i] = -1;
            }
        }
        while (!Q.empty()) {
            int u = Q.front(); Q.pop();
            for (auto it = edge[u].begin(); it != edge[u].end(); ++it) {
                int v = pair2[*it];
                if (v != -1 && level[v] < 0) {
                    level[v] = level[u] + 1;
                    Q.emplace(v);
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            vis[i] = false;
        }
        int d = 0;
        for (int i = 0; i < n; ++i) {
            if (pair1[i] == -1 && dfs(edge, i, level, &vis, &pair1, &pair2)) {
                ++d;
            }
        }
        if (d == 0) {
            return match;
        }
        match += d;
    }
}

int costume_change() {
    int N;
    cin >> N;
    vector<vector<int>> A(N, vector<int>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> A[i][j];
        }
    }
    int keep = 0;
    for (int color = -N; color <= N; ++color) {
        vector<vector<int>> edge(N);
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (A[i][j] == color) {
                    edge[i].emplace_back(j);
                }
            }
        }
        keep += hopcroftKarp(edge);
    }
    return N * N - keep;
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": " << costume_change() << endl;
    }
    return 0;
}
