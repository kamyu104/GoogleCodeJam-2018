# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Qualification Round - Problem A. Saving The Universe Again
# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard
#
# Time:  O(P)
# Space: O(P)
#

import collections

def count(P):
    exps, count = collections.defaultdict(int), 0
    for c in P:
        if c == 'C':
            count += 1
        else:
            exps[count] += 1
    max_exp, damages = 0, 0
    for exp, count in exps.iteritems():
        max_exp = max(max_exp, exp)
        damages += count*(2**exp)
    for i in reversed(xrange(1, max_exp)):
        exps[i] += exps[i+1]
    return exps, max_exp, damages 

def saving_the_universe_again():
    D, P = raw_input().strip().split()
    D = int(D)

    exps, max_exp, damages = count(P)
    hacks, to_reduce = 0, damages-D
    while max_exp > 0:
        if to_reduce <= 0:
            break
        to_reduce -= 2**(max_exp-1)
        exps[max_exp] -= 1
        if exps[max_exp] == 0:
            max_exp -= 1
        hacks += 1

    return hacks if to_reduce <= 0 else "IMPOSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, saving_the_universe_again())
