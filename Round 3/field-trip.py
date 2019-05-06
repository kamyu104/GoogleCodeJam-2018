# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 3 - Problem A. Field Trip
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007707/000000000004b7fe
#
# Time:  O(N)
# Space: O(1)
#

def field_trip():
    N = input()
    R = [0]*N
    C = [0]*N
    for i in xrange(N):
        R[i], C[i] = map(int, raw_input().strip().split())
    return max(((max(R)-min(R)+1)//2, (max(C)-min(C)+1)//2))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, field_trip())
