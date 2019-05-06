# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1A - Problem C. Edgy Baking
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007883/000000000002fff7
#
# Time:  O(N^2)
# Space: O(N)
#

import math

def merge_intervals(A, B):
    result = []
    i, j = 0, 0
    while i < len(A) or j < len(B):
        interval = None
        if j == len(B) or (i < len(A) and A[i][0] < B[j][0]):
            interval = A[i]
            i += 1
        else:
            interval = B[j]
            j += 1
        if not result or result[-1][1] < interval[0]:
            result.append(list(interval))
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result

def add_interval(S, interval, P_to_increase):
    new_S = []
    for s in S:
        if P_to_increase < s[0]+interval[0]:
            break
        new_S.append([s[0]+interval[0], s[1]+interval[1]])
    return merge_intervals(S, new_S)

def edgy_baking():
    N, P = map(int, raw_input().strip().split())
    W, H = [0]*N, [0]*N
    for i in xrange(N):
        W[i], H[i] = map(int, raw_input().strip().split())
    P_to_increase = P-2*(sum(W) + sum(H))
    S = [[0, 0]]
    for i in xrange(N):
        S = add_interval(S, [2*min(W[i], H[i]), 2*math.sqrt(W[i]**2 + H[i]**2)], P_to_increase)
    return P-max(0, P_to_increase-S[-1][1])

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, edgy_baking())
