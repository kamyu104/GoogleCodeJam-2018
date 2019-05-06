# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 2 - Problem B. Graceful Chainsaw Jugglers
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007706/00000000000459f3
#
# Time:  O(R^(4/3)*B^(4/3))
# Space: O(R^(4/3)*B^(4/3))
#

import collections
import sys

MAX_R, MAX_B = 500, 500

def memoization(V, i, r, b, lookup):
    if r < 0 or b < 0:
        return float("-inf")
    if i < 0:
        return 0
    key = i*(MAX_R+1)*(MAX_B+1)+r*(MAX_B+1)+b
    if lookup[key] is None:
        lookup[key] = max(memoization(V, i-1, r, b, lookup),
                          1 + memoization(V, i-1, r-V[i][0], b-V[i][1], lookup))
    return lookup[key]

def graceful_chainsaw_jugglers(V, lookup):
    R, B = map(int, raw_input().strip().split())
    return memoization(V, len(V)-1, R, B, lookup)

V = []
for i in xrange(MAX_R+1):
    if i*(i+1)//2 > MAX_R:
        break
    for j in xrange(MAX_B+1):
        if j*(j+1)//2 > MAX_B:
            break
        if (i, j) == (0, 0):
            continue
        if (j+1)*i*(i+1)//2 > MAX_R or (i+1)*j*(j+1)//2 > MAX_B:
            break
        V.append((i, j))
lookup = [None] * (len(V)+1)*(MAX_R+1)*(MAX_B+1)
sys.setrecursionlimit((len(V)+1)+(MAX_R+1)+(MAX_B+1))
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, graceful_chainsaw_jugglers(V, lookup))
