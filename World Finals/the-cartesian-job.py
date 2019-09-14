# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2018 World Finals - Problem C. Go, Gophers!
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004da2d
#
# Time:  O(K * N), K min of x s.t. 2^(-x) < epsilon => K = 53
# Space: O(K)
#

from sys import float_info
from math import atan2, pi

def crossprod(v1, v2):
    return v1[1]*v2[0] - v1[0]*v2[1]

def dotprod(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def real_angle(dotprod, crossprod):
    angle = atan2(crossprod, dotprod)
    if angle < 0:
        angle += 2*pi
    return 180*angle/pi

def angle(v1, v2):  # represented in |v1|*|v2|*cos(theta), |v1|*|v2|*sin(theta) form
    return (dotprod(v1, v2), crossprod(v1, v2))

def quadrant(v1):
    x, y = v1
    if x >= 0:
        return 1 if y >= 0 else 4
    return 2 if y >= 0 else 3

def compare_angle(v1, v2):
    q1, q2 = quadrant(v1), quadrant(v2)
    if q1 != q2:
        return -1 if q1 < q2 else 1
    return -1 if v2[0]*v1[1] < v1[0]*v2[1] else 1

def reflect_across_x(v):
    return (v[0], -v[1])

def min_angle(v1, v2):
    return v2 if compare_angle(v1, v2) != -1 else v1

def max_angle(v1, v2):
    return v2 if compare_angle(v1, v2) == -1 else v1

def compare_interval(interval_a, interval_b):
    x = real_angle(*interval_a[0]) < real_angle(*interval_b[0])
    y = compare_angle(interval_a[0], interval_b[0]) == -1
    if x != y:
        print x, y
        print real_angle(*interval_a[0]), real_angle(*interval_b[0])
        print interval_a[0], interval_b[0]
        assert(False)
    return compare_angle(interval_a[0], interval_b[0])

def dp(intervals):
    result = 0.0
    states = {}
    return result

def the_cartesian_job():
    N = input()
    intervals = []
    for _ in xrange(N):
        X0, Y0, X1, Y1 = map(int, raw_input().strip().split())
        interval = []
        for X2, Y2 in SEGMENT_POINTS:
            interval.append(angle((X1-X0, Y1-Y0), (X2-X0, Y2-Y0)))
        print map(lambda x: real_angle(*x), interval)
        interval = map(lambda x: min_angle(x, reflect_across_x(x)), interval)
        interval.sort(cmp=compare_angle)
        print map(lambda x: real_angle(*x), interval)
        print "-"*5
        intervals.append(interval)
    intervals.sort(cmp=compare_interval)
    print map(lambda x: [real_angle(*x[0]), real_angle(*x[1])], intervals)
    return dp(intervals)

# K = 0
# p = 1.0
# while p >= float_info.epsilon:
#     K += 1
#     p /= 2.0
# print K

SEGMENT_POINTS = [(0, 0), (0, 1000)]
for case in xrange(input()):
    print 'Case #%d: %.6f' % (case+1, the_cartesian_job())