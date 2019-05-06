# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1B - Problem B. Mysterious Road Signs
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007764/000000000003675b
#
# Time:  O(S)
# Space: O(1)
#

def mysterious_road_signs():
    M, N, start, xstart = range(4)
    S = input()

    max_size, count = 1, 1
    D, A, B = map(int, raw_input().strip().split())
    candidates = [[D+A, D-B, 0, 0] for _ in xrange(2)]

    for i in xrange(1, S):
        D, A, B = map(int, raw_input().strip().split())
        sign = [D+A, D-B]
        new_candidates = [None] * 2
        for m, n in [(M, N), (N, M)]:
            if sign[m] == candidates[m][m]:
                new_candidates[m] = candidates[m][:]
            elif sign[m] == candidates[n][m]:
                new_candidates[m] = candidates[n][:]
                new_candidates[m][xstart] = i
            else:
                new_candidates[m] = candidates[n][:]
                new_candidates[m][m] = sign[m]
                new_candidates[m][start] = new_candidates[m][xstart]
                new_candidates[m][xstart] = i
            size = i - new_candidates[m][start] + 1
            if max_size < size:
                max_size = size
                count = 1
            elif max_size == size and \
                 (not new_candidates[n] or
                  new_candidates[n][start] != new_candidates[m][start]):
                count += 1
        candidates = new_candidates
    return max_size, count

for case in xrange(input()):
    print "Case #{}: {} {}".format(case+1, *mysterious_road_signs())
