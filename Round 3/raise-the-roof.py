# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 3 - Problem C. Raise the Roof
# https://codejam.withgoogle.com/2018/challenges/0000000000007707/dashboard/000000000004b90d
#
# Time:  O(N^2)
# Space: O(N)
#

import math

Z_PLANE_NORMAL = (0, 0, 1)
X, Y, Z = range(3)

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

def negative(vector):
    return [-vector[0], -vector[1], -vector[2]]

def normalized(vector):
    l = length(vector)
    result = (vector[X]/l, vector[Y]/l, vector[Z]/l)
    if vector[Z] < 0:  # same direction with Z_PLANE_NORMAL
        return negative(result)
    return result

def find_next_column(columns, unused_columns_set, p, q, last_plane_normal):
    r = None
    curr_angle = None
    curr_plane_normal = None
    for i in unused_columns_set:
        # find r which minimizes the angle between the plane pqr and the last plane
        plane_normal = normalized(outer_product(vector(columns[q], columns[p]),
                                                vector(columns[q], columns[i])))
        crossprod = length(outer_product(plane_normal, last_plane_normal))
        dotprod = inner_product(plane_normal, last_plane_normal)
        angle = math.atan2(crossprod, dotprod)
        if curr_angle is None or curr_angle > angle:  # angle the smaller the better
            curr_angle = angle
            curr_plane_normal = plane_normal
            r = i
    return q, r, curr_plane_normal

def raise_the_roof():
    N = input()
    columns = [None]*N
    for i in xrange(N):
        columns[i] = tuple(map(int, raw_input().strip().split()))

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
    curr_angle = None
    pq = None
    for i in unused_columns_set:
        # find q which minimizes the angle between the vector pq and z-plane,
        vector_normal = negative(normalized(vector(columns[p], columns[i])))
        crossprod = length(outer_product(vector_normal, Z_PLANE_NORMAL))
        dotprod = inner_product(vector_normal, Z_PLANE_NORMAL)
        angle = math.atan2(crossprod, dotprod)
        if curr_angle is None or \
           curr_angle > angle:  # angle the smaller the better
            curr_angle = angle
            pq = vector_normal
            q = i
    unused_columns_set.remove(q)
    result.append(q+1)

    last_plane_normal = normalized(outer_product(pq, outer_product(pq, Z_PLANE_NORMAL)))
    while unused_columns_set:
        p, q, last_plane_normal = find_next_column(columns, unused_columns_set, p, q, last_plane_normal)
        unused_columns_set.remove(q)
        result.append(q+1)
    result.reverse()
    return " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, raise_the_roof())
