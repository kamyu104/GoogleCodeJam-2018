# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2018 World Finals - Problem E. The Cartesian Job
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004d962
#
# Time:  O(NlogN + K * N) = O(K * N), because K is much larger than logN (which is 14)
#                                   , K is min of x s.t. 2^(-(x-1)) < epsilon, thus K = 54
# Space: O(N)
#

from sys import float_info
from collections import defaultdict

def crossprod(v1, v2):
    return v1[1]*v2[0] - v1[0]*v2[1]

def dotprod(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def tan(v1, v2):  # tan(theta) represented in |v1|*|v2|*cos(theta), |v1|*|v2|*sin(theta) form
    return (dotprod(v1, v2), crossprod(v1, v2))

# Compute the cross product of vectors AB and AC
CW, COLLINEAR, CCW = range(-1, 2)
def ccw(A, B, C):
    area = (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])
    return CCW if area > 0 else CW if area < 0 else COLLINEAR

def compare_relative_tan(v1, v2):  # compare orientation, used before removing overlapped interval
    return -1 if ccw((0, 0), v1, v2) == CCW else 1

def compare_tan(v1, v2):  # compare theta, used after removing overlapped interval
    def quadrant(v):
        x, y = v
        if x >= 0:
            return 1 if y >= 0 else 4
        return 2 if y >= 0 else 3

    q1, q2 = quadrant(v1), quadrant(v2)
    if q1 != q2:
        return -1 if q1 < q2 else 1
    return -1 if v2[0]*v1[1] < v1[0]*v2[1] else 1

def min_tan(v1, v2):
    return v2 if compare_tan(v1, v2) != -1 else v1

def max_tan(v1, v2):
    return v2 if compare_tan(v1, v2) == -1 else v1

def reflect_across_x(v):
    return (v[0], -v[1])

def compare_interval(interval_a, interval_b):
    return compare_tan(interval_a[0], interval_b[0])

def no_overlapped_interval(interval, s, e):
    interval.sort(cmp=compare_relative_tan)
    no_overlapped_interval = sorted(map(lambda x: min_tan(x, reflect_across_x(x)), interval),
                                    cmp=compare_relative_tan)
    if compare_relative_tan((1, 0), interval[0]) != -1 and \
       compare_relative_tan(interval[1], (1, 0)) != -1:
        # overlapped around theta = 0
        if compare_relative_tan(s, no_overlapped_interval[0]) == -1:
            s = no_overlapped_interval[0]
    elif compare_relative_tan((-1, 0), interval[0]) != -1 and \
         compare_relative_tan(interval[1], (-1, 0)) != -1:
         # overlapped around theta = pi/2
         if compare_relative_tan(no_overlapped_interval[1], e) == -1:
            e = no_overlapped_interval[1]
    return no_overlapped_interval, s, e

def sort_and_clean(intervals, s, e):  # sort and keep intervals in [s, e]
    result = []
    for interval in intervals:
        if compare_relative_tan(interval[0], s) == -1:
            interval[0] = s
        if compare_relative_tan(e, interval[1]) == -1:
            interval[1] = e
        if compare_relative_tan(interval[1], interval[0]) == -1:
            continue
        result.append(interval)
    result.sort(cmp=compare_interval)  # O(NlogN)
    return result

def dp(intervals, s, e):  # find probability of not covering all [s, e]
    result = 0.0
    states = defaultdict(float)
    states[(s, s)] = 1.0
    intervals.append([e, e])  # end of intervals
    for a, b in intervals:
        assert(len(states) <= K)  # only largest K probs would be kept,
                                  # and the number of states increases at most one each time
        new_states = defaultdict(float)
        for (s1, s2), p in states.iteritems():
            if compare_tan(s1, a) == -1:
                result += p
                continue
            if p < float_info.epsilon:
                continue
            new_states[tuple(sorted([max_tan(s1, b), s2], cmp=compare_tan))] += p/2
            new_states[tuple(sorted([s1, max_tan(s2, b)], cmp=compare_tan))] += p/2
        assert(len(new_states)-len(states) <= 1)
        states = new_states
    return result

def the_cartesian_job():
    N = input()
    intervals = []
    s, e = (1, 0), (-1, 0)
    for _ in xrange(N):
        X0, Y0, X1, Y1 = map(int, raw_input().strip().split())
        interval = []
        for X2, Y2 in SEGMENT_POINTS:
            interval.append(tan((X1-X0, Y1-Y0), (X2-X0, Y2-Y0)))
        interval, s, e = no_overlapped_interval(interval, s, e)
        intervals.append(interval)
    intervals = sort_and_clean(intervals, s, e)
    return dp(intervals, s, e)

K = 54
SEGMENT_POINTS = [(0, 0), (0, 1000)]
for case in xrange(input()):
    print 'Case #%d: %.6f' % (case+1, the_cartesian_job())
