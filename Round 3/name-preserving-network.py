# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 3 - Name-Preserving Network
# https://codejam.withgoogle.com/2018/challenges/0000000000007707/dashboard/000000000004ba29
#
# Time:  O(L^2 * logL)
# Space: O(L^2)
#

import sys
import collections
import random
import itertools

def random_generate_graph(C):
    while True:
        array = range(C)*4
        random.shuffle(array)
        G = [[0 for _ in xrange(C)] for _ in xrange(C)]
        for i in xrange(0, len(array), 2):
            if array[i] != array[i+1] and \
            G[array[i]][array[i+1]] == 0 and \
            G[array[i+1]][array[i]] == 0:
                G[array[i]][array[i+1]], G[array[i+1]][array[i]] = 1, 1
            else:
                break
        else:
            break
    return G

def get_signature(G):
    def matrix_expo(A, K):
        def matrix_mult(A, B):
            ZB = zip(*B)
            return [[sum(a*b for a, b in itertools.izip(row, col)) \
                        for col in ZB] for row in A]

        if K == 0:
            return [[int(i==j) for j in xrange(len(A))] \
                    for i in xrange(len(A))]
        if K == 1:
            return A
        if K % 2:
            return matrix_mult(matrix_expo(A, K-1), A)
        B = matrix_expo(A, K//2)
        return matrix_mult(B, B)

    MAGIC = 7
    matrix_expo(G, MAGIC)
    return map(tuple, map(sorted, matrix_expo(G, MAGIC)))

def generate_graph(L, U):
    while True:
        G = random_generate_graph(L)
        sig = get_signature(G)
        if len(set(sig)) == len(G):
            break
    return G, sig

def inv_idx(array):
    result = collections.defaultdict(int)
    for i in xrange(len(array)):
        result[array[i]] = i
    return result

def name_preserving_network():
    L, U = map(int, raw_input().strip().split())

    G, sig = generate_graph(L, U)
    print len(G)
    for i in xrange(len(G)):
        for j in xrange(i+1, len(G[i])):
            if G[i][j]:
                print i+1, j+1
    sys.stdout.flush()

    permuted_G = [[0 for j in xrange(len(G[i]))] for i in xrange(len(G))]
    N = input()
    for _ in xrange(2*N):
        i, j = map(int, raw_input().strip().split())
        permuted_G[i-1][j-1], permuted_G[j-1][i-1] = 1, 1

    result = []
    inv_sig = inv_idx(get_signature(permuted_G))
    for i in xrange(len(sig)):
        result.append(inv_sig[sig[i]]+1)
    print " ".join(map(str, result))
    sys.stdout.flush()

t = input()
for case in xrange(t):
    name_preserving_network()
