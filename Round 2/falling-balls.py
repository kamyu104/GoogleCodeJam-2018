# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 2 - Problem A. Falling Balls
# https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard
#
# Time:  O(C^2)
# Space: O(C^2)
#

def falling_balls():
    C = input()
    B = map(int, raw_input().strip().split())
    if B[0] == 0 or B[-1] == 0:
        return "IMPOSSIBLE"
    result = [['.']*C]
    c = 0
    for r in xrange(len(B)):
        if B[r] == 0:
            continue
        target, left, right = r, c, c+B[r]-1
        c += B[r]
        if left < target:
            for r in xrange(target-left):
                result[r][left+r] = '\\'
                if r == len(result)-1:
                    result.append(['.']*C)
        if right > target:
            for r in xrange(right-target):
                result[r][right-r] = '/'
                if r == len(result)-1:
                    result.append(['.']*C)
    return str(len(result)) + "\n" + "\n".join(["".join(row) for row in result])

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, falling_balls())
