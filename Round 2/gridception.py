# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 2 - Problem D. Gridception
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/00000000000459f4
#
# Time:  O(2^4 * R^2 * C^2), fail in PyPy2
# Space: O(R * C)
#

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def expected_color(color, r, c, i, j):
    if i < r and j < c:
        return 1 if (color & 1) else 0
    elif i < r and j >= c:
        return 1 if (color & 2) else 0
    elif i >= r and j < c:
        return 1 if (color & 4) else 0
    else:
        return 1 if (color & 8) else 0

def dfs(grid, color, r, c, i, j, lookup):
    if not (0 <= i < len(grid) and 0 <= j < len(grid[i]) and
            lookup[i][j] == False and
            grid[i][j] == expected_color(color, r, c, i, j)):
        return 0
    lookup[i][j] = True
    result = 1
    for d in directions:
        result += dfs(grid, color, r, c, i+d[0], j+d[1], lookup)
    return result

def gridception():
    R, C = map(int, raw_input().strip().split())
    grid = [[0 for _ in xrange(C)] for _ in xrange(R)]
    for r in xrange(R):
        for c, color in enumerate(raw_input().strip()):
            if color == 'W':
                grid[r][c] = 1
    result = 0
    colors = set()
    for r in xrange(R):
        for c in xrange(C):
            colors.add(grid[r][c]*15)
            if r+1 < R:
                colors.add(grid[r][c]*3+grid[r+1][c]*12)
            if c+1 < C:
                colors.add(grid[r][c]*5+grid[r][c+1]*10)
            if r+1 < R and c+1 < C:
                colors.add(grid[r][c]+grid[r][c+1]*2+grid[r+1][c]*4+grid[r+1][c+1]*8)
    for color in colors:
        for r in xrange(R+1):
            for c in xrange(C+1):
                lookup = [[False for _ in xrange(C)] for _ in xrange(R)] 
                for i in xrange(R):
                    for j in xrange(C):
                        result = max(result, dfs(grid, color, r, c, i, j, lookup))
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, gridception())
