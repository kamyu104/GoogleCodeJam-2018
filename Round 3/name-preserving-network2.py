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

def random_generate_graph(N):
    array = range(N)*4
    while True:
        random.shuffle(array)
        edges = set()
        for i in xrange(0, len(array), 2):
            if array[i] != array[i+1] and \
              (array[i], array[i+1]) not in edges and \
              (array[i+1], array[i]) not in edges:
                edges.add((array[i], array[i+1]))
            else:
                break
        else:
            break
    return edges

def get_signature(edges):
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
    N = len(edges)//2
    G = [[0 for _ in xrange(N)] for _ in xrange(N)]
    for i, j in edges:
        G[i][j], G[j][i] = 1, 1
    matrix_expo(G, MAGIC)
    return map(tuple, map(sorted, matrix_expo(G, MAGIC)))

def generate_graph(L, U):
    while True:
        edges = random_generate_graph(L)
        sig = get_signature(edges)
        if len(set(sig)) == len(edges)//2:
            break
    return edges, sig

def inv_idx(array):
    result = collections.defaultdict(int)
    for i in xrange(len(array)):
        result[array[i]] = i
    return result

def name_preserving_network():
    L, U = map(int, raw_input().strip().split())
    edges, sig = generate_graph(L, U)
    print len(edges)//2
    for i, j in edges:
        print i+1, j+1
    sys.stdout.flush()

    permuted_edges = set()
    N = input()
    for _ in xrange(2*N):
        i, j = map(int, raw_input().strip().split())
        permuted_edges.add((i-1, j-1))
    result = []
    inv_sig = inv_idx(get_signature(permuted_edges))
    for i in xrange(len(sig)):
        result.append(inv_sig[sig[i]]+1)
    print " ".join(map(str, result))
    sys.stdout.flush()

T = input()
for case in xrange(T):
    name_preserving_network()
