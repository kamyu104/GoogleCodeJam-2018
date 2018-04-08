# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Qualification Round - Problem D. Cubic UFO
# https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cc
#
# Time:  O(1)
# Space: O(1)
#

import math

def matrix_multi(A, B):
    result = [[0.0 for _ in xrange(len(B[0]))] for _ in xrange(len(A))]
    for i in xrange(len(A)):
        for k in xrange(len(A[0])):
            if A[i][k] == 0.0:
                continue
            for j in xrange(len(B[0])):
                result[i][j] += A[i][k] * B[k][j]
    return result

def rotate_y(matrix, cosx):
    sinx = math.sqrt(1.0-cosx**2)
    Ry = [[cosx, 0.0, -sinx],
          [ 0.0, 1.0,   0.0],
          [sinx, 0.0,  cosx]]
    return matrix_multi(matrix, Ry)
    
def rotate_x(matrix, cosx):
    sinx = math.sqrt(1.0-cosx**2)
    Rx = [[1.0,   0.0,  0.0],
          [0.0,  cosx, sinx],
          [0.0, -sinx, cosx]]
    return matrix_multi(matrix, Rx)

def cubic_ufo():
    A = float(input())

    # sqrt(2)*sinx + cosx = A
    cosx = (A + math.sqrt(2*(3-A**2)))/3
    matrix = [[0.5, 0.0, 0.0],
              [0.0, 0.5, 0.0],
              [0.0, 0.0, 0.5]]
    matrix = rotate_y(matrix, 1.0/math.sqrt(2))
    matrix = rotate_x(matrix, cosx)
    return matrix

for case in xrange(input()):
    print 'Case #%d:' % (case+1)
    for center in cubic_ufo():
        print " ".join(map(str, center))