# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Qualification Round - Problem B. Trouble Sort
# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb
#
# Time:  O(NlogN)
# Space: O(N)
#

def trouble_sort():
    N = input()
    V = map(int, raw_input().strip().split())

    sorted_V = [V[i::2] for i in xrange(2)]
    sorted_V[0].sort(), sorted_V[1].sort()
    for i in xrange(len(V)-1):
        if sorted_V[i%2][i//2] > sorted_V[(i+1)%2][(i+1)//2]:
            return i
    return "OK"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, trouble_sort())
