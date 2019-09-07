# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2018 World Finals - Problem A. Jurisdiction Restrictions
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004dbbd
#
# Time:  O(2^(S * 2)), pass in PyPy2 but Python2
# Space: O(2^S)
#

def jurisdiction_restrictions():
    R, C, S = map(int, raw_input().strip().split())
    Rs, Cs, Ds = [0]*S, [0]*S, [0]*S
    for i in xrange(S):
        Rs[i], Cs[i], Ds[i] = map(int, raw_input().strip().split())
        Rs[i] -= 1
        Cs[i] -= 1

    intersections = [0]*(2**S)
    for i in xrange(1, len(intersections)):
        min_r, max_r = 0, R
        min_c, max_c = 0, C
        bitmask = 1
        for j in xrange(S):
            if i & bitmask:
                min_r, max_r = max(min_r, Rs[j]-Ds[j]), min(max_r, Rs[j]+Ds[j]+1)
                min_c, max_c = max(min_c, Cs[j]-Ds[j]), min(max_c, Cs[j]+Ds[j]+1)
            bitmask <<= 1
        if not (min_r < max_r and min_c < max_c):
            continue
        intersections[i] = (max_r-min_r)*(max_c-min_c)
        for j in xrange(S):
            intersections[i] -= int(min_r <= Rs[j] < max_r and
                                    min_c <= Cs[j] < max_c)
    areas = [0]*len(intersections)
    for i in xrange(1, len(areas)):
        s = i
        while s:  # inclusion-exclusion principle
            areas[i] += (-1)**(COUNT_OF_ONE[s]%2+1) * intersections[s]
            s = (s-1)&i  # at most 14,316,139 times if S = 15
    min_p, max_p = R*C, 0
    for i in xrange(1, len(areas)):
        min_p = min(min_p, areas[i]//COUNT_OF_ONE[i])  # floor(areas[i]/count)
        max_p = max(max_p, (areas[-1]-areas[-1-i]-1)//COUNT_OF_ONE[i]+1)  # ceil((areas[all]-areas[all^i])/count)
    return max_p-min_p

def count_of_one(n):
    result = 0
    while n:
        n &= n-1
        result += 1
    return result

MAX_S = 15
COUNT_OF_ONE = [count_of_one(i) for i in xrange(2**MAX_S)]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, jurisdiction_restrictions())
