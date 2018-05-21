// Copyright (c) 2018 kamyu. All rights reserved.

/*
 * Google Code Jam 2018 Round 2 - Problem D. Gridception
 * https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard/00000000000459f4
 *
 * Time:  O(2^4 * R^2 * C^2)
 * Space: O(R * C)
 *
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <unordered_set>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::max;
using std::pair;
using std::unordered_set;


int expected_color(int color, int r, int c, int i, int j) {
    if (i < r && j < c) {
        return (color & 1) ? 1 : 0;
    } else if (i < r && j >= c) {
        return (color & 2) ? 1 : 0;
    } else if (i >= r && j < c) {
        return (color & 4) ? 1 : 0;
    } else {
        return (color & 8) ? 1 : 0;
    }
}

int dfs(const vector<vector<int>>& grid, int color,
        int r, int c,
        int i, int j,
        vector<vector<bool>> *lookup) {
    if (!(0 <= i && i < grid.size() &&
          0 <= j && j < grid[i].size() &&
          (*lookup)[i][j] == false &&
          grid[i][j] == expected_color(color, r, c, i, j))) {
        return 0;
    }
    (*lookup)[i][j] = true;
    int result = 1;
    static const vector<pair<int, int>> directions{{-1, 0}, {1, 0},
                                                   {0, -1}, {0, 1}};
    for (const auto& d : directions) {
        result += dfs(grid, color, r, c, i + d.first, j + d.second, lookup);
    }
    return result;
}

int gridception() {
    int R, C;
    cin >> R >> C;
    vector<vector<int>> grid(R, vector<int>(C));
    for (int r = 0; r < R; ++r) {
        for (int c = 0; c < C; ++c) {
            char color;
            cin >> color;
            if (color == 'W') {
                grid[r][c] = 1;
            }
        }
    }
    int result = 0;
    unordered_set<int> colors;
    for (int r = 0; r < R; ++r) {
        for (int c = 0; c < C; ++c) {
            colors.emplace(grid[r][c] * 15);
            if (r + 1 < R) {
                colors.emplace(grid[r][c] * 3 + grid[r + 1][c] * 12);
            }
            if (c + 1 < C) {
                colors.emplace(grid[r][c] * 5 + grid[r][c + 1] * 10);
            }
            if (r + 1 < R && c + 1 < C) {
                colors.emplace(grid[r][c] + grid[r][c + 1] * 2 +
                               grid[r + 1][c] * 4 + grid[r + 1][c + 1] * 8);
            }
        }
    }
    for (const auto& color : colors) {
        for (int r = 0; r <= R; ++r) {
            for (int c = 0; c <= C; ++c) {
                vector<vector<bool>> lookup(R, vector<bool>(C));
                for (int i = 0; i < R; ++i) {
                    for (int j = 0; j < C; ++j) {
                        result = max(result,
                                     dfs(grid, color, r, c, i, j, &lookup));
                    }
                }
            }
        }
    }
    return result;
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": " << gridception() << endl;
    }
    return 0;
}
