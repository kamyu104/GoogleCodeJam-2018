# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1B- Problem C. Transmutation
# https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard/000000000003675c
#
# Time:  O(M^3 * logS)
# Space: O(M^2)
#

import collections
import copy

def multiply(R, k):
    tmp = copy.deepcopy(R)
    for i in tmp:
        tmp[i] *= k
    return tmp

def add(R1, R2):
    for i in R2:
        R1[i] += R2[i]

def find_debt(G):
    for i in xrange(len(G)):
        if G[i] < 0:
            return i
    return len(G)

def impossible(L, R, G):
    R, G = copy.deepcopy(R), G[:]
    G[0] -= L
    if G[0] >= 0:
        return False
    i = 0
    while i != len(G):
        if i in R[i] or G[i]+sum(G) < 0:
            return True
        add(G, multiply(R[i], G[i]))
        G[i] = 0
        for Rj in R.values():
            if i in Rj:
                add(Rj, multiply(R[i], Rj[i]))
                Rj.pop(i)
        R.pop(i)
        i = find_debt(G)
    return False

def transmutation():
    M = input()
    R = collections.defaultdict(lambda: collections.defaultdict(int))
    for i in xrange(M):
        R1, R2 = map(int, raw_input().strip().split())
        R[i][R1-1] = R[i][R2-1] = 1
    G = map(int, raw_input().strip().split())

    left, right = 0, sum(G)
    while left <= right:
        mid = left + (right-left)//2
        if impossible(mid, R, G):
            right = mid-1
        else:
            left = mid+1
    return left-1
    
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, transmutation())
