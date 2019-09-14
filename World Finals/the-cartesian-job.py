# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2018 World Finals - Problem E. The Cartesian Job
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004d962
#
# Time:  O(K * N), K is min of x s.t. 2^(-x) < epsilon => K = 53
# Space: O(K)
#

from sys import float_info
from collections import defaultdict
from math import atan2, pi

def crossprod(v1, v2):
    return v1[1]*v2[0] - v1[0]*v2[1]

def dotprod(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def theta(dotprod, crossprod):
    theta = atan2(crossprod, dotprod)
    if theta < 0:
        theta += 2*pi
    return 180*theta/pi

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def tan(v1, v2):  # tan(theta) represented in |v1|*|v2|*cos(theta), |v1|*|v2|*sin(theta) form
    x, y = dotprod(v1, v2), crossprod(v1, v2)
    g = gcd(abs(x), abs(y))
    return (x//g, y//g)

def quadrant(v1):
    x, y = v1
    if x >= 0:
        return 1 if y >= 0 else 4
    return 2 if y >= 0 else 3

def compare_tan(v1, v2):
    q1, q2 = quadrant(v1), quadrant(v2)
    if q1 != q2:
        return -1 if q1 < q2 else 1
    return -1 if v2[0]*v1[1] < v1[0]*v2[1] else 1

def reflect_across_x(v):
    return (v[0], -v[1])

def min_tan(v1, v2):
    return v2 if compare_tan(v1, v2) != -1 else v1

def max_tan(v1, v2):
    return v2 if compare_tan(v1, v2) == -1 else v1

def compare_interval(interval_a, interval_b):
    debug(interval_a[0], interval_b[0])
    return compare_tan(interval_a[0], interval_b[0])

def debug(a, b):
    x = theta(*a) < theta(*b)
    y = (compare_tan(a, b) == -1)
    if x != y:
        print x, y
        print theta(*a), theta(*b)
        print a, b
        assert(False)

def dp(intervals):
    result = 0.0
    s = intervals[0][0]
    states = defaultdict(float)
    states[(s, s)] = 1.0
    for a, b in intervals:
        assert(len(states) <= K)
        #print "prob", map(lambda x: (map(lambda y: theta(*y), x[0]), x[1]), states.iteritems()), "interval", [theta(*a), theta(*b)]
        new_states = defaultdict(float)
        for (s1, s2), p in states.iteritems():
            debug(s1, a)
            if compare_tan(s1, a) == -1:
                #print theta(*s1), theta(*a)
                result += p
                continue
            if p < float_info.epsilon:
                continue
            new_states[tuple(sorted([max_tan(s1, b), s2], cmp=compare_tan))] += p/2
            new_states[tuple(sorted([s1, max_tan(s2, b)], cmp=compare_tan))] += p/2
        states = new_states
    # print "prob", map(lambda x: (map(lambda y: theta(*y), x[0]), x[1]), states.iteritems())
    return result

def the_cartesian_job():
    N = input()
    intervals = []
    for _ in xrange(N):
        X0, Y0, X1, Y1 = map(int, raw_input().strip().split())
        interval = []
        for X2, Y2 in SEGMENT_POINTS:
            interval.append(tan((X1-X0, Y1-Y0), (X2-X0, Y2-Y0)))
        interval = map(lambda x: min_tan(x, reflect_across_x(x)), interval)  # remove overlapped area
        interval.sort(cmp=compare_tan)
        intervals.append(interval)
    intervals.append([(-1, 0), (-1, 0)])  # end of intervals
    intervals.sort(cmp=compare_interval)
    #print map(lambda x: [theta(*x[0]), theta(*x[1])], intervals)
    return dp(intervals)

K = 53
SEGMENT_POINTS = [(0, 0), (0, 1000)]
for case in xrange(input()):
    print 'Case #%d: %.6f' % (case+1, the_cartesian_job())
