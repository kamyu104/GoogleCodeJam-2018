# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1A - Problem B. Bit Party
# https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard/000000000002fff6
#
# Time:  O(ClogC * log(max(S)*B+max(P)))
# Space: O(C)
#

def check(T, R, B, M, S, P):
    C = [0]*len(M)
    for i in xrange(len(C)):
        C[i] = max(0, min(M[i], (T-P[i])//S[i]))  # S[i] * N + P[i] <= T
    C.sort(reverse=True)  # O(ClogC), getting top R of C could be improved
                          # to O(C) by using quick select (std::nth_element in C++)
    return sum(C[:R]) >= B

def bit_party():
    R, B, C = map(int, raw_input().strip().split())
    M, S, P = [0]*C, [0]*C, [0]*C
    for i in xrange(C):
        M[i], S[i], P[i] =  map(int, raw_input().strip().split())
    left, right = 0, max(S)*B + max(P)
    while left <= right:
        mid = left + (right-left)//2
        if check(mid, R, B, M, S, P):
            right = mid-1
        else:
            left = mid+1
    return left

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, bit_party())
