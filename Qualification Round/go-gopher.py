# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Qualification Round - Problem C. Go, Gopher!
# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/0000000000007a30
#
# Time:  O(P)
# Space: O(1)
#

import sys

def deploy(A, i, j):
    lookup = set()
    while len(lookup) < 9:
        print i, j
        sys.stdout.flush()
        ni, nj = map(int, raw_input().strip().split())
        if (ni, nj) == (-1, -1):  # error
            exit()
        if (ni, nj) == (0, 0):  # done
            return True
        lookup.add((ni-i+1)*3 + (nj-j+1))
    return False

def go_gohper():
    A = input()
    i = 2
    while True:
        if deploy(A, i, 2):
            break
        A -= 9
        i += 3

for case in xrange(input()):
    go_gohper()
