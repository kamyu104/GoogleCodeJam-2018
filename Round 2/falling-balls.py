# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 2 - Problem A. Falling Balls
# https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard
#
# Time:  O(C^2)
# Space: O(C^2)
#

def falling_balls():
    TARGET, LEFT, RIGHT = range(3)
    C = input()
    B = map(int, raw_input().strip().split())
    if B[0] == 0 or B[-1] == 0:
        return "IMPOSSIBLE"
    groups = []
    c = 0
    for r in xrange(len(B)):
        if B[r] > 0:
            groups.append((r, c, c+B[r]-1))
            c += B[r]
    result = [['.']*C]
    for group in groups:
        if group[LEFT] < group[TARGET]:
            for r in xrange(group[TARGET]-group[LEFT]):
                result[r][group[LEFT]+r] = '\\'
                if r == len(result)-1:
                    result.append(['.']*C)
        if group[RIGHT] > group[TARGET]:
            for r in xrange(group[RIGHT]-group[TARGET]):
                result[r][group[RIGHT]-r] = '/'
                if r == len(result)-1:
                    result.append(['.']*C)
    return str(len(result)) + "\n" + "\n".join(["".join(row) for row in result])

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, falling_balls())
