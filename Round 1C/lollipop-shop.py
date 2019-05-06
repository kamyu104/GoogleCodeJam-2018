# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1C - Problem B. Lollipop Shop
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007765/000000000003e068
#
# Time:  O(N^2)
# Space: O(N)
#

import sys
import random

def sell(statistics, stock, prefs):
    if prefs:
        for i in prefs:
            statistics[i] += 1
        least_flavors = []
        for i in prefs:
            if i in stock:
                if not least_flavors or \
                   statistics[least_flavors[0]] > statistics[i]:
                    least_flavors = [i]
                elif statistics[least_flavors[0]] == statistics[i]:
                    least_flavors.append(i)
        if least_flavors:
            i = random.randint(0, len(least_flavors)-1)
            stock.discard(least_flavors[i])
            print least_flavors[i]
            sys.stdout.flush()
            return
    print -1
    sys.stdout.flush()

def lollipop_shop():
    N = input()
    stock = set(range(N))
    statistics = [0]*N
    for _ in xrange(1, N+1):
        prefs = map(int, raw_input().strip().split())
        sell(statistics, stock, prefs[1:])

for case in xrange(input()):
    lollipop_shop()
