# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2018 World Finals - Problem A. Jurisdiction Restrictions
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000007766/000000000004dbbd
#
# Time:  O(S^6 * log(R * C)), pass in PyPy2 but Python2
# Space: O(S^2)
#

from collections import deque

# Time:  O(V^2 * E)
# Space: O(V + E)
class Dinic(object):
    def __init__(self, n):
        self.adj = [[] for _ in xrange(n)]
    
    def add_edge(self, i, j, c):
        self.adj[i].append([j, c, len(self.adj[j])])
        self.adj[j].append([i, 0, len(self.adj[i]) - 1])

    def max_flow(self, S, T):
        def bfs(S, T, adj, lev):  # Time: O(E), levelize
            for i in xrange(len(adj)):
                lev[i] = -1
            lev[S] = 0
            q = deque([S])
            while q:
                v = q.popleft()
                for i in xrange(len(adj[v])):
                    to, cap, rev = adj[v][i]
                    if cap and lev[to] == -1:
                        lev[to] = lev[v] + 1
                        q.append(to)
            return lev[T] != -1

        def dfs(S, T, v, f, adj, lev, done):  # Time: O(V * E), augment
            if v == T or not f:
                return f
            while done[v] < len(adj[v]):
                to, cap, rev = adj[v][done[v]]
                if lev[to] > lev[v]:
                    t = dfs(S, T, to, min(f, cap), adj, lev, done)
                    if t > 0:
                        adj[to][rev][1] += t
                        adj[v][done[v]][1] -= t
                        return t
                done[v] += 1
            return 0

        adj = self.adj
        V = len(self.adj)
        f = 0
        lev = [-1] * V
        while bfs(S, T, adj, lev):  # at most O(V) times
            done = [0] * V
            while True:
                t = dfs(S, T, S, float("inf"), adj, lev, done)
                if t == 0:
                    break
                f += t
        return f

def check(S, areas, neighbors, p, expected_flow):  # V = S^2, E = S^2, Time:  O(V^2 * E) = O(S^6)
    s = len(areas)+S
    t = s+1
    dinic = Dinic(t+1)
    for i in xrange(S):
        dinic.add_edge(s, i, p)
        for a in neighbors[i]:
            dinic.add_edge(i, a+S, areas[a])
    for a in xrange(len(areas)):
        dinic.add_edge(a+S, t, areas[a])
    return dinic.max_flow(s, t) == expected_flow

def jurisdiction_restrictions():
    R, C, S = map(int, raw_input().strip().split())
    Rs, Cs, Ds = [0]*S, [0]*S, [0]*S
    for i in xrange(S):
        Rs[i], Cs[i], Ds[i] = map(int, raw_input().strip().split())
        Rs[i] -= 1
        Cs[i] -= 1

    rows_set, cols_set = set([0, R]), set([0, C])
    for i in xrange(S):
        rows_set.add(max(Rs[i]-Ds[i], 0))
        rows_set.add(min(Rs[i]+Ds[i]+1, R))
        cols_set.add(max(Cs[i]-Ds[i], 0))
        cols_set.add(min(Cs[i]+Ds[i]+1, C))
    rows, cols = sorted(rows_set), sorted(cols_set)

    areas, neighbors, total_area = [], [[] for _ in xrange(S)], 0
    for i in xrange(len(rows)-1):
        for j in xrange(len(cols)-1):
            area = (rows[i+1]-rows[i])*(cols[j+1]-cols[j])
            for k in xrange(S):
                if rows[i] <= Rs[k] < rows[i+1] and \
                   cols[j] <= Cs[k] < cols[j+1]:
                    area -= 1
            is_used = False
            for k in xrange(S):
                if abs(rows[i]-Rs[k]) <= Ds[k] and abs(cols[j]-Cs[k]) <= Ds[k]:
                   is_used = True
                   neighbors[k].append(len(areas))
            if is_used:
                areas.append(area)
                total_area += area

    left, right = 0, R*C
    while left <= right:
        mid = left +(right-left)//2
        if check(S, areas, neighbors, mid, total_area):
            right = mid-1
        else:
            left = mid+1
    max_p = left

    left, right = 0, max_p
    while left <= right:
        mid = left +(right-left)//2
        if not check(S, areas, neighbors, mid, mid*S):
            right = mid-1
        else:
            left = mid+1
    min_p = right

    return max_p-min_p

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, jurisdiction_restrictions())
