# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1B- Problem C. Transmutation
# https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard/000000000003675c
#
# Time:  O(M^3 * logS)
# Space: O(M^2)
#

def multiply(R, k):
    return [g*k for g in R]

def add(L1, L2):
    for i in xrange(len(L1)):
        L1[i] += L2[i]

def replace(R, i):
    for Rj in R:
        if Rj[i] != 0:
            add(Rj, multiply(R[i], Rj[i]))
            Rj[i] = 0

def find_debt(G):
    for i in xrange(len(G)):
        if G[i] < 0:
            return i
    return len(G)

def impossible(L, R, G):
    R, G = [Ri[:] for Ri in R], G[:]
    i = 0
    G[i] -= L
    while i != len(G) and G[i] < 0:
        if R[i][i] != 0 or G[i]+sum(G) < 0:
            return True
        add(G, multiply(R[i], G[i]))
        G[i] = 0
        replace(R, i)
        R[i] = [0] * len(G)
        i = find_debt(G)
    return False

def transmutation():
    M = input()
    R = []
    for _ in xrange(M):
        R1, R2 = map(int, raw_input().strip().split())
        Ri = [0] * M
        Ri[R1-1] = Ri[R2-1] = 1
        R.append(Ri)
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
