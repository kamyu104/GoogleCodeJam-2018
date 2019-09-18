# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2018 World Finals - Problem D. Swordmaster
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004d961
#
# Time:  O(N * P)
# Space: O(N * P)
#

# [Definition]
# - D1: set(our attacks) > set(his defenses, set(our defenses) >= set(his attacks)
# - D2: set(our attacks) <= set(his defenses, set(our defenses) < set(his attacks)
# - D3: set(our attacks) > set(his defenses, set(our defenses) < set(his attacks)
# - D4: set(our attacks) <= set(his defenses, set(our defenses) >= set(his attacks)
# - G1: nobody outside G1 could defend any duelists inside G1 if only if remaining duelists only in D2 or D3
# - G2: nobody outside G2 could attack any duelists inside G2 only if remaining duelists only in D2 or D4

from sys import setrecursionlimit
from collections import defaultdict

# modified Tarjan's algorithm
def leaf_strongly_connected_components(graph):  # Time: O(|V| + |E|), Space: O(|V|)
    def strongconnect(v, index_counter, index, lowlinks, stack, stack_set, result):
        is_leaf_found = False  # extra flags to find leaf SCCs
        index[v] = index_counter[0]
        lowlinks[v] = index_counter[0]
        index_counter[0] += 1
        stack_set.add(v)
        stack.append(v)
        for w in (graph[v] if v in graph else []):
            if w not in index:
                if strongconnect(w, index_counter, index, lowlinks, stack, stack_set, result):
                    is_leaf_found = True
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif w in stack_set:
                lowlinks[v] = min(lowlinks[v], index[w])
            else:  # visited child but not in curr stack
                is_leaf_found = True
        if lowlinks[v] == index[v]:
            connected_component = []
            w = None
            while w != v:
                w = stack.pop()
                stack_set.remove(w)
                connected_component.append(w)
            if not is_leaf_found:  # only keeps leaf SCCs
                is_leaf_found = True
                result.append(tuple(connected_component))
        return is_leaf_found

    index_counter, index, lowlinks = [0], {}, {}
    stack, stack_set = [], set()
    result = []
    for node in graph:
        if node not in index:
            strongconnect(node, index_counter, index, lowlinks, stack, stack_set, result)
    return result

def any_G1(A, D):
    G1 = set(range(1, len(A)))
    attacks_to_duelists, duelists_to_attacks = defaultdict(set), defaultdict(set)
    for i in xrange(1, len(A)):
        for a in A[i]:
            attacks_to_duelists[a].add(i)
            duelists_to_attacks[i].add(a)
    delta_D_set = set(D[0])
    while delta_D_set:  # BFS, Time: O(input_size) <= O(N * P), Space: O(input_size) <= O(N * P) to find G1
        new_delta_D_set = set()
        for d in delta_D_set:
            for j in attacks_to_duelists[d]:
                duelists_to_attacks[j].remove(d)
                if duelists_to_attacks[j]:
                    continue
                duelists_to_attacks.pop(j)
                G1.remove(j)
                new_delta_D_set |= set(D[j])
            attacks_to_duelists.pop(d)
        delta_D_set = new_delta_D_set
    return G1

def any_G2(A, D):
    graph = defaultdict(list)
    A_set = reduce(set.union, (set(A[i]) for i in xrange(1, len(A))))
    for i in xrange(1, len(A)):  # Time: O(N * P), Space: O(N * P) to construct graph
        D_set = set(D[i])
        for a in A[i]:
            graph[-a].append(i)  # attack node represented as negative number
        for a in A_set:
            if a not in D_set:
                graph[i].append(-a)  # attack node represented as negative number
    for leaf_scc in leaf_strongly_connected_components(graph):  # Time: O(N * P), Space: O(N + P) to find leaf SCC
        # G2 exists if only if valid leaf SCC of G2 exists, which is also a minimal G2
        duelists_set = set(i for i in leaf_scc if i > 0)
        D_set = reduce(set.intersection, (set(D[i]) for i in duelists_set))
        if any(all(a not in D_set for a in A[i]) for i in duelists_set) or \
           any(a not in D_set for a in A[0]):
            continue
        return leaf_scc  # minimal G2

def swordmaster():
    N, P = map(int, raw_input().strip().split())
    A, D = [], []
    for _ in xrange(N):
        _, _ = map(int, raw_input().strip().split())
        A.append(map(int, raw_input().strip().split()))
        D.append(map(int, raw_input().strip().split()))
    return "NO" if any_G1(A, D) or any_G2(A, D) else "YES"

N, P = 1000, 1000
setrecursionlimit(N-1+P+2)  # ulimit -S -s unlimited
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, swordmaster())
