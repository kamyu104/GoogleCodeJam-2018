# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 3 - Problem C. Raise the Roof
# https://codejam.withgoogle.com/2018/challenges/0000000000007707/dashboard/000000000004b90d
#
# Time:  O(N^2)
# Space: O(N)
#

import math

def inner_product(vector1, vector2):
    return vector1[X]*vector2[X] + vector1[Y]*vector2[Y] + vector1[Z]*vector2[Z]

def outer_product(vector1, vector2):
    return (vector1[Y]*vector2[Z]-vector1[Z]*vector2[Y], 
            vector1[Z]*vector2[X]-vector1[X]*vector2[Z], 
            vector1[X]*vector2[Y]-vector1[Y]*vector2[X])

def vector(point1, point2):
    return (point2[X]-point1[X], point2[Y]-point1[Y], point2[Z]-point1[Z])

def length(vector):
    return math.sqrt(vector[X]**2 + vector[Y]**2 + vector[Z]**2)

def normalized(vector):
    l = length(vector)
    result = (vector[X]/l, vector[Y]/l, vector[Z]/l)
    if inner_product(result, NORMAL_Z) < 0:
        return (-vector[X]/l, -vector[Y]/l, -vector[Z]/l)
    return result

def find_next_column(columns, unused_columns_set, p, q, last_normal):
    r_less_than_90 = None
    r_more_than_90 = None
    curr_normal_less_than_90 = None
    curr_normal_more_than_90 = None
    for i in unused_columns_set:
        # find r which minimizes the angle between the plane pqr and the last plane
        normal = normalized(outer_product(vector(columns[q], columns[p]), \
                                          vector(columns[q], columns[i])))
        if inner_product(normal, last_normal) > 0:
            if curr_normal_less_than_90 is None or \
                length(outer_product(curr_normal_less_than_90, last_normal)) > \
                length(outer_product(normal, last_normal)):
                curr_normal_less_than_90 = normal
                r_less_than_90 = i
        else:
            if curr_normal_more_than_90 is None or \
                length(outer_product(curr_normal_more_than_90, last_normal)) < \
                length(outer_product(normal, last_normal)):
                curr_normal_more_than_90 = normal
                r_more_than_90 = i
    return q, \
           r_less_than_90 if r_less_than_90 is not None else r_more_than_90, \
           curr_normal_less_than_90 if curr_normal_less_than_90 is not None else curr_normal_more_than_90

def fence_construction():
    N = input()
    
    columns = [None]*(N)
    for i in xrange(N):
        columns[i]= tuple(map(int, raw_input().strip().split()))

    result = []
    unused_columns_set = set(range(N))
    p = None
    for i in unused_columns_set:
        # find the p which is the tallest
        if p is None or \
           columns[p][Z] < columns[i][Z]:
            p = i
    unused_columns_set.remove(p)
    result.append(p+1)

    q = None
    pq = None
    for i in unused_columns_set:
        # find q which minimizes the angle between the vector pq and z-plane
        normal = normalized(vector(columns[p], columns[i]))
        if pq is None or \
           length(outer_product(pq, NORMAL_Z)) < \
           length(outer_product(normal, NORMAL_Z)):
            pq = normal
            q = i
    unused_columns_set.remove(q)
    result.append(q+1)

    last_normal = normalized(outer_product(pq, outer_product(pq, NORMAL_Z)))
    while unused_columns_set:
        p, q, last_normal = find_next_column(columns, unused_columns_set, p, q, last_normal)
        unused_columns_set.remove(q)
        result.append(q+1)
    result.reverse()
    return " ".join(map(str, result))

NORMAL_Z = (0, 0, 1)
X, Y, Z = range(3)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fence_construction())
